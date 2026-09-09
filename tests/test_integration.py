from text_analyzer.analyzer import analyze_text
from text_analyzer.file_loader import load_text_file


def test_load_and_analyze_text(tmp_path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text(
        "hello world\nhello",
        encoding="utf-8",
    )

    text = load_text_file(str(file_path))
    stats = analyze_text(text)

    assert stats.characters == 17
    assert stats.words == 3
    assert stats.lines == 2
    assert stats.unique_words == 2