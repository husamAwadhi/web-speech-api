import pytest
import webspeech.utils.strings as strings


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hello, World", "Hello World"),
        ("me?", "me"),
    ],
)
def test_clean_default(text, expected):
    assert strings.clean(text) == expected


@pytest.mark.parametrize(
    "text, expected, bad_chars",
    [
        ("perfect match", "perfectmatch", [" "]),
        ("sweet nothings", "sweet nothings", ["?"]),
        ("BBC", "BB", ["C"]),
    ],
)
def test_clean(text, expected, bad_chars):
    assert strings.clean(text, bad_chars) == expected
