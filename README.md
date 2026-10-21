# simple_screaming_snake_case

A focused Python utility that converts identifier names between camelCase, PascalCase, snake_case, and SCREAMING_SNAKE_CASE. Standard library only, zero dependencies.

## Usage

```python
from simple_screaming_snake_case import (
    to_screaming_snake,
    camel_to_screaming_snake,
    pascal_to_screaming_snake,
    snake_to_screaming_snake,
    screaming_snake_to_camel,
    screaming_snake_to_pascal,
    screaming_snake_to_snake,
)

to_screaming_snake("camelCase")      # "CAMEL_CASE"
to_screaming_snake("PascalCase")     # "PASCAL_CASE"
to_screaming_snake("snake_case")     # "SNAKE_CASE"

camel_to_screaming_snake("parseHTTPSConnection")  # "PARSE_HTTPS_CONNECTION"
pascal_to_screaming_snake("HTTPServer")           # "HTTP_SERVER"

screaming_snake_to_camel("SCREAMING_SNAKE_CASE")  # "screamingSnakeCase"
screaming_snake_to_pascal("SCREAMING_SNAKE_CASE") # "ScreamingSnakeCase"
screaming_snake_to_snake("SCREAMING_SNAKE_CASE")  # "screaming_snake_case"
```

## Why this exists

The specific problem: converting between the four common identifier conventions in Python projects that also touch JavaScript or configuration files, without pulling in a heavy string-utilities package. The trade-off is that `to_screaming_snake` is a single-direction normalizer — it accepts any of the four conventions and emits SCREAMING_SNAKE_CASE, but the reverse conversions (`screaming_snake_to_camel` etc.) operate only on well-formed SCREAMING_SNAKE input. If you need round-trip fidelity, convert to screaming snake first, then to your target.

## Edge cases you will hit

Acronyms embedded in camelCase are the main awkward spot. `HTTPServer` becomes `HTTP_SERVER` (the library splits at the upper-run-to-lower transition, so the trailing lowercase letters start a new word). `parseHTTPSConnection` becomes `PARSE_HTTPS_CONNECTION`. Digits are treated as standalone word tokens: `user2Admin` becomes `USER_2_ADMIN`, and `3rdParty` becomes `3_RD_PARTY`. Leading and trailing underscores are stripped, and consecutive underscores collapse to a single separator. The empty string returns the empty string for every function.

## Running tests

```bash
PYTHONPATH=src python -m unittest discover -s tests
```
