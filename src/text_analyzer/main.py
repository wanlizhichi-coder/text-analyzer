import logging

from .analyzer import analyze_text
from .config import LOG_LEVEL
from .exceptions import TextLoadError
from .file_loader import load_text_file


logger = logging.getLogger(__name__)


def configure_logging() -> None:
    logging.basicConfig(
        level=LOG_LEVEL,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )


def main() -> None:
    configure_logging()

    logger.info("Application started")

    file_path = input("请输入txt文件路径：")

    try:
        text = load_text_file(file_path)
        stats = analyze_text(text)

    except TextLoadError as exc:
        print(exc)
        return

    except ValueError as exc:
        print(f"无法分析文本：{exc}")
        return

    print(f"字符数：{stats.characters}")
    print(f"单词数：{stats.words}")
    print(f"非空行数：{stats.lines}")
    print(f"平均单词长度：{stats.average_word_length:.2f}")
    print(f"最长单词：{stats.longest_word}")

    logger.info("Application finished")


if __name__ == "__main__":
    main()