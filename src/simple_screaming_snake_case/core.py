import re

__all__ = [
    "camel_to_screaming_snake",
    "pascal_to_screaming_snake",
    "snake_to_screaming_snake",
    "screaming_snake_to_camel",
    "screaming_snake_to_pascal",
    "screaming_snake_to_snake",
    "to_screaming_snake",
]


# Precompiled regexes. There are two distinct word-boundary patterns in camelCase
# and PascalCase input:
#   - a lower/upper junction (camelCase -> camel_Case)
#   - an upper-run thinning (HTTPSKey -> HTTPS_Key)
# Handling these with two passes keeps the substitution logic simple and
# testable. A single-pass regex that tries to encode both rules becomes hard
# to reason about and tends to mishandle 'HTTPServer'.
_LOWER_UPPER = re.compile(r"(?<=[a-z0-9])(?=[A-Z])")
_UPPER_RUN = re.compile(r"(?<=[A-Z])(?=[A-Z][a-z])")


def _split_words(identifier: str) -> list[str]:
    """Split a camelCase / PascalCase / snake_case / SCREAMING identifier into words.

    Underscores and digits are treated as word boundaries. Within a contiguous
    run of letters, lower-to-upper transitions and upper-run-to-lower
    transitions also mark boundaries.
    """
    words: list[str] = []
    current: list[str] = []
    prev = ""
    for ch in identifier:
        if ch == "_":
            if current:
                words.append("".join(current))
                current = []
            prev = ""
            continue
        if ch.isdigit():
            if current and not (len(current) == 1 and current[0].isdigit()):
                words.append("".join(current))
                current = []
            current.append(ch)
            prev = "digit"
            continue
        if not ch.isascii() or not ch.isalpha():
            # Non-ASCII, non-digit char in an identifier. We still consume it
            # into the current word so output stays one-to-one with input
            # length, even though such inputs are out of scope.
            current.append(ch)
            prev = ch
            continue
        if prev == "digit" and not current:
            current = [ch]
        if prev and prev.isalpha() and prev.isupper() and ch.islower() and len(current) > 1:
            # Upper-run -> lower: e.g. 'HTTPS' + 'erver' — emit everything but
            # the last upper char, keep the last as the start of the new word.
            words.append("".join(current[:-1]))
            current = [current[-1], ch]
        elif prev and prev.islower() and ch.isupper():
            # lower -> upper: standard camelCase boundary.
            words.append("".join(current))
            current = [ch]
        elif prev == "digit":
            words.append("".join(current))
            current = [ch]
        else:
            current.append(ch)
        prev = ch
    if current:
        words.append("".join(current))
    return [w for w in words if w]


def to_screaming_snake(identifier: str) -> str:
    """Convert any supported case convention to SCREAMING_SNAKE_CASE.

    This is the general entry point. It accepts camelCase, PascalCase,
    snake_case, or SCREAMING_SNAKE_CASE and produces SCREAMING_SNAKE_CASE.
    Empty string input returns an empty string.
    """
    if not identifier:
        return ""
    words = _split_words(identifier)
    return "_".join(w.upper() for w in words)


def camel_to_screaming_snake(identifier: str) -> str:
    """Convert camelCase to SCREAMING_SNAKE_CASE."""
    return to_screaming_snake(identifier)


def pascal_to_screaming_snake(identifier: str) -> str:
    """Convert PascalCase to SCREAMING_SNAKE_CASE."""
    return to_screaming_snake(identifier)


def snake_to_screaming_snake(identifier: str) -> str:
    """Convert snake_case to SCREAMING_SNAKE_CASE."""
    return to_screaming_snake(identifier)


def screaming_snake_to_camel(identifier: str) -> str:
    """Convert SCREAMING_SNAKE_CASE to camelCase.

    The first word is lowercased; subsequent words are title-cased.
    """
    if not identifier:
        return ""
    words = [w for w in identifier.split("_") if w]
    if not words:
        return ""
    camel = words[0].lower()
    for w in words[1:]:
        camel += w[:1].upper() + w[1:].lower()
    return camel


def screaming_snake_to_pascal(identifier: str) -> str:
    """Convert SCREAMING_SNAKE_CASE to PascalCase.

    Each word is title-cased (first letter upper, rest lower) and joined
    without separators.
    """
    if not identifier:
        return ""
    words = [w for w in identifier.split("_") if w]
    return "".join(w[:1].upper() + w[1:].lower() for w in words)


def screaming_snake_to_snake(identifier: str) -> str:
    """Convert SCREAMING_SNAKE_CASE to snake_case."""
    if not identifier:
        return ""
    return identifier.lower()
