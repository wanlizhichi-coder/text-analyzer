from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)

@dataclass
class TextStats:
    characters: int
    words: int
    lines: int
    average_word_length: float
    longest_word: str
    unique_words: int


def analyze_text(text: str) -> TextStats:
    if not text.strip():
        raise ValueError("文本不能为空")

    logger.debug("Text analysis completed")
    words = text.split()

    lines = [
        line
        for line in text.splitlines()
        if line.strip()
    ]

    if words:
        average_word_length = sum(len(word) for word in words) / len(words)
        longest_word = max(words, key=len)
        unique_words = len(set(words))
    else:
        average_word_length = 0.0
        longest_word = ""
        unique_words = 0

    return TextStats(
        characters=len(text),
        words=len(words),
        lines=len(lines),
        average_word_length=average_word_length,
        longest_word=longest_word,
        unique_words=unique_words
    )