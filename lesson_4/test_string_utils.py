import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" skypro", "skypro"),  # пробел перед словом
    ("   hello", "hello"),  # несколько пробелов перед словом
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),  # нет пробела - нечего удалять
    ("     ", ""),  # множественные пробелы удаляются
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol", [
    ("skypro", "s"),  # нижний регистр
    ("Hello", "H"),  # верхний регистр
])
def test_contains_positive(string, symbol):
    assert string_utils.contains(string, symbol) is True


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol", [
    ("skypro", "z"),  # нижний регистр
    ("hello", "H"),  # верхний регистр
])
def test_contains_negative(string, symbol):
    assert not string_utils.contains(string, symbol)


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected_result", [
    ("Hello", "l", "Heo"),
    ("World", "w", "orld"),
])
def test_delete_symbol_positive(string, symbol, expected_result):
    assert string_utils.delete_symbol(string, symbol) == expected_result


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected_result", [
    ("Hello", "a", "Hello"),
])
def test_delete_symbol_negative(string, symbol, expected_result):
    assert string_utils.delete_symbol(string, symbol) == expected_result
