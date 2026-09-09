import pytest

from text_analyzer.analyzer import analyze_text


def test_analyze_text_returns_correct_stats_for_normal_text():
    text = "hello world\nhello"

    stats = analyze_text(text)

    assert stats.characters == 17
    assert stats.non_whitespace_characters == 15
    assert stats.words == 3
    assert stats.lines == 2
    assert stats.average_word_length == 5.0
    assert stats.longest_word == "hello"
    assert stats.unique_words == 2


def test_analyze_text_handles_single_word():
    stats = analyze_text("Python")

    assert stats.characters == 6
    assert stats.non_whitespace_characters == 6
    assert stats.words == 1
    assert stats.lines == 1
    assert stats.average_word_length == 6.0
    assert stats.longest_word == "Python"
    assert stats.unique_words == 1


@pytest.mark.parametrize(
    "text",
    [
        "",
        " ",
        "\n",
        "\t",
        "   \n\t",
    ],
)
def test_analyze_text_raises_value_error_for_blank_text(text):
    with pytest.raises(ValueError):
        analyze_text(text)