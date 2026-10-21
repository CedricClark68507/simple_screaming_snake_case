import unittest

from simple_screaming_snake_case import (
    camel_to_screaming_snake,
    pascal_to_screaming_snake,
    snake_to_screaming_snake,
    screaming_snake_to_camel,
    screaming_snake_to_pascal,
    screaming_snake_to_snake,
    to_screaming_snake,
)


class TestToScreamingSnake(unittest.TestCase):
    def test_camel_case(self):
        self.assertEqual(camel_to_screaming_snake("camelCase"), "CAMEL_CASE")

    def test_pascal_case(self):
        self.assertEqual(pascal_to_screaming_snake("PascalCase"), "PASCAL_CASE")

    def test_snake_case(self):
        self.assertEqual(snake_to_screaming_snake("snake_case"), "SNAKE_CASE")

    def test_already_screaming(self):
        self.assertEqual(to_screaming_snake("ALREADY_SCREAMING"), "ALREADY_SCREAMING")

    def test_single_word(self):
        self.assertEqual(to_screaming_snake("word"), "WORD")

    def test_acronym_prefix(self):
        self.assertEqual(to_screaming_snake("HTTPServer"), "HTTP_SERVER")

    def test_acronym_middle(self):
        self.assertEqual(to_screaming_snake("parseHTTPSConnection"), "PARSE_HTTPS_CONNECTION")

    def test_digit_transition(self):
        self.assertEqual(to_screaming_snake("user2Admin"), "USER_2_ADMIN")

    def test_leading_digit(self):
        self.assertEqual(to_screaming_snake("3rdParty"), "3_RD_PARTY")

    def test_consecutive_digits(self):
        self.assertEqual(to_screaming_snake("level42Status"), "LEVEL_42_STATUS")

    def test_leading_underscores_stripped(self):
        self.assertEqual(to_screaming_snake("__privateField"), "PRIVATE_FIELD")

    def test_empty_string(self):
        self.assertEqual(to_screaming_snake(""), "")


class TestFromScreamingSnake(unittest.TestCase):
    def test_to_camel(self):
        self.assertEqual(screaming_snake_to_camel("SCREAMING_SNAKE_CASE"), "screamingSnakeCase")

    def test_to_pascal(self):
        self.assertEqual(screaming_snake_to_pascal("SCREAMING_SNAKE_CASE"), "ScreamingSnakeCase")

    def test_to_snake(self):
        self.assertEqual(screaming_snake_to_snake("SCREAMING_SNAKE_CASE"), "screaming_snake_case")

    def test_to_camel_single_word(self):
        self.assertEqual(screaming_snake_to_camel("CONSTANT"), "constant")

    def test_to_pascal_single_word(self):
        self.assertEqual(screaming_snake_to_pascal("CONSTANT"), "Constant")

    def test_to_snake_single_word(self):
        self.assertEqual(screaming_snake_to_snake("CONSTANT"), "constant")

    def test_to_camel_acronym_preserved_as_word(self):
        self.assertEqual(screaming_snake_to_camel("HTTP_SERVER"), "httpServer")

    def test_to_pascal_acronym_preserved_as_word(self):
        self.assertEqual(screaming_snake_to_pascal("HTTP_SERVER"), "HttpServer")

    def test_to_camel_digit_word(self):
        self.assertEqual(screaming_snake_to_camel("USER_2_TOKEN"), "user2Token")

    def test_to_camel_empty(self):
        self.assertEqual(screaming_snake_to_camel(""), "")

    def test_to_camel_only_underscores(self):
        self.assertEqual(screaming_snake_to_camel("___"), "")

    def test_to_snake_empty(self):
        self.assertEqual(screaming_snake_to_snake(""), "")


if __name__ == "__main__":
    unittest.main()
