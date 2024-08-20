import pytest
from webspeech.score.score import calculate, match_ratio, calculate_fluency


@pytest.mark.parametrize(
    "word1, word2, expected",
    [
        ("perfect match", "perfect match", 1),
        ("ABC ltd", "ABC limited", 0.64),
        ("BBC", "ABC", 0.67),
        ("Fast track systems", "Fastrack systems", 0.89),
        ("BTAT", "BT", 0.5),
        ("Gemini Partners", "Gemmini Partners", 0.94),
        ("", "", 0),
        ("", "Hi", 0),
        ("Hi", "", 0),
    ],
)
def test_partials(word1, word2, expected):
    assert match_ratio(word1, word2) == expected


@pytest.mark.parametrize(
    "wpm, expected",
    [
        (120, 100),
        (110, 100),
        (107, 90),
        (91, 80),
        (88, 80),
        (72, 70),
        (69, 60),
        (56, 50),
        (47, 40),
        (30, 30),
        (23, 20),
        (18, 10),
        (3, 0),
    ],
)
def test_fluency(wpm, expected):
    assert calculate_fluency(wpm, False) == expected


@pytest.mark.parametrize(
    "base, transcript, duration, expected",
    [
        (  # 1
            "Hello World Hello",
            "Hello World Hello",
            1,
            {
                "fluency": "5.0",
                "wpm": "180.0",
                "content": "5.0",
                "pronunciation": "5.0",
            },
        ),
        (  # 2
            "Hello. World, Hello",
            "Hello World Hello",
            1,
            {
                "fluency": "5.0",
                "wpm": "180.0",
                "content": "5.0",
                "pronunciation": "5.0",
            },
        ),
        (  # 3
            "Hello World Hello",
            "Hello Hello",
            1,
            {
                "fluency": "5.0",
                "wpm": "120.0",
                "content": "3.4",
                "pronunciation": "5.0",
            },
        ),
        (  # 4
            "Hello World Hello",
            "world hello man",
            1,
            {
                "fluency": "5.0",
                "wpm": "120.0",
                "content": "3.4",
                "pronunciation": "5.0",
            },
        ),
        (  # 5
            "Hello Hello woman",
            "hello hello man",
            1,
            {
                "fluency": "5.0",
                "wpm": "180.0",
                "content": "5.0",
                "pronunciation": "3.4",
            },
        ),
        (  # 6
            "Hello Hello smoke",
            "hello hello man",
            1,
            {
                "fluency": "5.0",
                "wpm": "120.0",
                "content": "3.4",
                "pronunciation": "5.0",
            },
        ),
        (  # 7
            "I am going to meet Alice tomorrow for lunch",
            "I am going to meet Alice for brunch",
            3,
            {
                "fluency": "5.0",
                "wpm": "160.0",
                "content": "4.5",
                "pronunciation": "4.4",
            },
        ),
        (  # 8
            "I am going to meet Alice tomorrow for lunch",
            "I am going to meet Alice tomorrow for brunch",
            3,
            {
                "fluency": "5.0",
                "wpm": "180.0",
                "content": "5.0",
                "pronunciation": "4.5",
            },
        ),
        (  # 9
            "I am going to meet Alice tomorrow for lunch",
            "Bob tomorrow for brunch",
            3,
            {"fluency": "3.0", "wpm": "60.0", "content": "1.7", "pronunciation": "3.4"},
        ),
        (  # 10
            "I am going to meet Alice tomorrow for lunch",
            "Bob tomorrow for brunch",
            20,
            {"fluency": "0.2", "wpm": "9.0", "content": "1.7", "pronunciation": "3.4"},
        ),
    ],
)
def test_calculation(base, transcript, duration, expected):
    score = calculate(base, transcript, duration)
    assert score["fluency"] == expected["fluency"]
    assert score["wpm"] == expected["wpm"]
    assert score["content"] == expected["content"]
    assert score["pronunciation"] == expected["pronunciation"]


@pytest.mark.parametrize(
    "base, transcript, expected",
    [
        (
            "Hello World",
            "Hello World",
            [{"word": "hello", "type": "match"}, {"word": "world", "type": "match"}],
        ),
        ("Hello", "Helloo", [{"word": "hello", "type": "partial"}]),
        (
            "Hello man",
            "Helloo",
            [{"word": "hello", "type": "partial"}, {"word": "man", "type": "mismatch"}],
        ),
        (
            "Speedy Hello man",
            "Hello man",
            [
                {"word": "speedy", "type": "mismatch"},
                {"word": "hello", "type": "match"},
                {"word": "man", "type": "match"},
            ],
        ),
    ],
)
def test_comparison_result(base, transcript, expected):
    score = calculate(base, transcript, 1)
    assert score["result"] == expected
