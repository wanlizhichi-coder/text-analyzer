import subprocess
import sys


def test_cli_analyzes_text_file_successfully(tmp_path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text(
        "hello world\nhello",
        encoding="utf-8",
    )

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "text_analyzer.main",
        ],
        input=f"{file_path}\n",
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0
    assert "单词" in result.stdout
    assert "3" in result.stdout


def test_cli_returns_nonzero_for_missing_file(tmp_path):
    file_path = tmp_path / "missing.txt"

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "text_analyzer.main",
        ],
        input=f"{file_path}\n",
        text=True,
        capture_output=True,
        check=False,
    )

    combined_output = result.stdout + result.stderr

    assert result.returncode != 0
    assert "不存在" in combined_output