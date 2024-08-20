import pytest
from webspeech.score.result import Result


@pytest.mark.parametrize(
    "words_dict, expected",
    [
        (
            [
                {"word": "perfect", "type": "match"},
                {"word": "perfecto", "type": "mismatch"},
            ],
            [
                {"type": "match", "word": "perfect"},
                {"type": "mismatch", "word": "perfecto"},
            ],
        ),
        (
            [
                {"word": "perfect", "type": "partial"},
                {"word": "perfecto", "type": "mismatch"},
            ],
            [
                {"type": "partial", "word": "perfect"},
                {"type": "mismatch", "word": "perfecto"},
            ],
        ),
    ],
)
def test_result_summary(words_dict, expected):
    r = Result()
    for item in words_dict:
        if item["type"] == "partial":
            r.add_partial(item["word"])
        elif item["type"] == "match":
            r.add_match(item["word"])
        else:
            r.add_mismatch(item["word"])

    assert r.summary() == expected


@pytest.mark.parametrize(
    "words_dict, expected",
    [
        (
            [
                {"word": "perfect", "type": "match"},
                {"word": "perfecto", "type": "mismatch"},
                {"word": "perfecto", "type": "partial"},
            ],
            [1, 1, 1],
        ),
        (
            [
                {"word": "perfect", "type": "partial"},
                {"word": "perfecto", "type": "mismatch"},
                {"word": "perfectoo", "type": "mismatch"},
            ],
            [0, 2, 1],
        ),
    ],
)
def test_count(words_dict, expected):
    r = Result()
    for item in words_dict:
        if item["type"] == "partial":
            r.add_partial(item["word"])
        elif item["type"] == "match":
            r.add_match(item["word"])
        else:
            r.add_mismatch(item["word"])

    assert [r.match_count(), r.mismatch_count(), r.partial_count()] == expected
