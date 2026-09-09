import logging

from text_analyzer.analyzer import analyze_text
from text_analyzer.config import LOG_LEVEL
from text_analyzer.exceptions import TextLoadError
from text_analyzer.file_loader import load_text_file


logger = logging.getLogger(__name__)


def configure_logging() -> None:
    logging.basicConfig(
        level=getattr(logging, LOG_LEVEL.upper(), logging.INFO),
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )


def main() -> int:
    configure_logging()

    path = input("请输入文本文件路径：").strip()

    try:
        text = load_text_file(path)
        stats = analyze_text(text)
    except (TextLoadError, ValueError) as exc:
        logger.error("%s", exc)
        return 1

    print(f"字符数：{stats.characters}")
    print(f"非空白字符数：{stats.non_whitespace_characters}")
    print(f"单词数：{stats.words}")
    print(f"行数：{stats.lines}")
    print(f"平均单词长度：{stats.average_word_length:.2f}")
    print(f"最长单词：{stats.longest_word}")
    print(f"不同单词数：{stats.unique_words}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())