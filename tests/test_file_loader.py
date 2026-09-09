import pytest

from text_analyzer.exceptions import TextLoadError
from text_analyzer.file_loader import load_text_file


@pytest.fixture
def sample_text_file(tmp_path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("hello world", encoding="utf-8")
    return file_path


def test_load_text_file_returns_file_content(sample_text_file):
    text = load_text_file(str(sample_text_file))

    assert text == "hello world"


def test_load_text_file_raises_text_load_error_when_file_does_not_exist(
    tmp_path,
):
    file_path = tmp_path / "missing.txt"

    with pytest.raises(TextLoadError):
        load_text_file(str(file_path))


def test_load_text_file_raises_text_load_error_when_path_is_directory(
    tmp_path,
):
    with pytest.raises(TextLoadError):
        load_text_file(str(tmp_path))


def test_load_text_file_raises_text_load_error_for_invalid_utf8(tmp_path):
    file_path = tmp_path / "invalid.txt"
    file_path.write_bytes(b"\xff\xfe\xfa")

    with pytest.raises(TextLoadError):
        load_text_file(str(file_path))


def test_load_text_file_raises_text_load_error_for_permission_error(
    monkeypatch,
):
    def fake_open(*args, **kwargs):
        raise PermissionError("Permission denied")

    monkeypatch.setattr("builtins.open", fake_open)

    with pytest.raises(TextLoadError) as exc_info:
        load_text_file("secret.txt")

    assert isinstance(exc_info.value.__cause__, PermissionError)