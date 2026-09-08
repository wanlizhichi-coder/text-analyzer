import logging

from .exceptions import TextLoadError


logger = logging.getLogger(__name__)


def load_text_file(path: str) -> str:
    logger.debug("Attempting to load text file: %s", path)

    try:
        with open(path, mode="r", encoding="utf-8") as file:
            text = file.read()

    except FileNotFoundError as exc:
        logger.warning("File not found: %s", path)
        raise TextLoadError(f"文件不存在：{path}") from exc 

    except PermissionError as exc:
        logger.error("Permission denied while reading file: %s", path)
        raise TextLoadError(f"没有权限读取文件：{path}") from exc

    except IsADirectoryError as exc:
        logger.warning("Expected file but received directory: %s", path)
        raise TextLoadError(f"输入的是目录而不是文件：{path}") from exc

    except UnicodeDecodeError as exc:
        logger.warning("Invalid UTF-8 file: %s", path)
        raise TextLoadError(
            f"文件不是有效的 UTF-8 文本：{path}"
        ) from exc

    logger.info("Successfully loaded text file: %s", path)

    return text