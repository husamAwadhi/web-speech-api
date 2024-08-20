import difflib
import math
from .result import Result
from webspeech.utils.strings import clean, match_ratio
from webspeech.utils.floats import scale


def calculate(base: str, transcript: str, duration: float) -> dict:
    """
    Calculate the similarity between two transcripts.

    Args:
        base (str): The base transcript.
        transcript (str): The transcript to compare to the base.

    Returns:
        dict: Score summary.
    """
    clean_base = clean(base).lower()

    result = Result()
    lib = difflib.Differ()

    clean_list = clean_base.split()
    diff = lib.compare(clean_list, transcript.lower().split())

    potential_partial = {"word": "", "index": None}
    for index, line in enumerate(diff):
        # additional / partial match from user input
        if potential_partial["index"] is not None:
            # carry potential partial over
            if line.startswith("?"):
                continue
            elif line.startswith("+"):
                distance = match_ratio(potential_partial["word"], line[2:].strip())
                if distance >= 0.3:
                    result.add_partial(potential_partial["word"])
                else:
                    result.add_mismatch(potential_partial["word"])
            else:
                result.add_mismatch(potential_partial["word"])
            potential_partial = {"word": "", "index": None}

        # missing word from user input
        if line.startswith("-"):
            potential_partial = {"word": line[2:].strip(), "index": index}
        # matches
        elif not line.startswith(("?", "+")):
            result.add_match(line[2:].strip())

    # flush
    if potential_partial["index"] is not None:
        result.add_mismatch(potential_partial["word"])

    wpm = ((result.match_count() + result.partial_count()) / duration) * 60
    fluency = calculate_fluency(wpm)
    content = calculate_content_score(
        result.match_count(), result.partial_count(), len(clean_list)
    )
    pronunciation = calculate_pronunciation_score(
        result.match_count(), result.partial_count()
    )

    return {
        "wpm": "{:.1f}".format(wpm),
        "fluency": "{:.1f}".format(fluency),
        "content": "{:.1f}".format(content),
        "pronunciation": "{:.1f}".format(pronunciation),
        "overall": "{:.1f}".format((fluency + content + pronunciation) / 3),
        "result": result.summary(),
    }


def calculate_fluency(words_per_min: float, scale_score: bool = True) -> int:
    """
    Get the similarity fluency based on the Number of words spoken correctly per minute.

    Args:
        words_per_min (float): The the Number of words spoken correctly per minute.

    Returns:
        int: The similarity fluency.
    """
    if words_per_min >= 110:
        score = 100
    elif words_per_min >= 100:
        score = 90
    elif words_per_min >= 90:
        score = 80
    elif words_per_min >= 10:
        score = int(math.floor(words_per_min / 10.0)) * 10
    elif words_per_min >= 5:
        score = 5
    else:
        score = 0

    return scale(score, 5) if scale_score else score


def calculate_content_score(
    correct_words_count: int, partial_words_count: int, total_words_count: int
) -> float:
    """
    Calculate the content score.

    Args:
        correct_words_count (int): The correct words count.
        partial_words_count (int): The partially correct words count.
        total_words_count (int): The total words count.

    Returns:
        float: The content score.
    """
    return scale(
        (
            round((correct_words_count + partial_words_count) / total_words_count, 2)
            if total_words_count > 0
            else 0.0
        ),
        5,
        1,
    )


def calculate_pronunciation_score(
    correct_words_count: int, partial_words_count: int
) -> float:
    """
    Calculate the pronunciation score.

    Args:
        correct_words_count (int): The correct words count.
        partial_words_count (int): The partial words count.

    Returns:
        float: The pronunciation score.
    """
    return scale(
        (
            round(correct_words_count / (correct_words_count + partial_words_count), 2)
            if (correct_words_count + partial_words_count) > 0
            else 0.0
        ),
        5,
        1,
    )
