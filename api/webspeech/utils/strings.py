def clean(
    text: str, bad_chars: list[str] = [";", ":", "!", "*", ".", ",", "?", "(", ")"]
) -> str:
    """
    Remove bad characters from a string

    Args:
        text (str): The string to clean
        bad_chars (list): The characters to remove

    Returns:
        str: The cleaned string

    Examples:
        >>> clean("Hello, world!", [",", " "])
        'Helloworld!'

    """

    return "".join(filter(lambda i: i not in bad_chars, text))


def match_ratio(base_string: str, input_string: str) -> float:
    """
    Calculate match ratio between 2 strings. The comparison determines
    how closely two values match each other by calculating the
    Character Edit Distance between two String values, and also taking
    into account the length of the longer or shorter of the two values,
    by character count.

    Link:
        https://www.oracle.com/webfolder/technetwork/data-quality/edqhelp/content/processor_library/matching/comparisons/character_match_percentage.htm

    Args:
        base_string (str): The first word.
        input_string (str): The second word.

    Returns:
        float: character match
    """

    base_length = len(base_string)
    input_length = len(input_string)
    if min(base_length, input_length) == 0:
        return 0

    distance = (
        edit_distance(base_string, input_string)
        if base_length >= input_length
        else edit_distance(input_string, base_string)
    )

    return round(
        (max(base_length, input_length) - distance) / max(base_length, input_length), 2
    )


def edit_distance(string1: str, string2: str, ignore_case: bool = True) -> int:
    """
    Calculate the edit distance between two words.

    Args:
        string1 (str): The first word. (base)
        string2 (str): The second word.
        ignore_case (bool): Whether to ignore case.

    Returns:
        int: The edit distance.
    """
    if ignore_case:
        string1 = string1.lower()
        string2 = string2.lower()
    if len(string1) == 0 or len(string2) == 0 or string1 == string2:
        return 0

    m, n = len(string1), len(string2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif string1[i - 1] == string2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[m][n]
