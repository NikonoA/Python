import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("alex", "Alex"), ("hello world", "Hello world")])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" Alex", "Alex"), (" 12345", "12345"),
    (" !!!!####", "!!!!####"), (" hello world", "hello world")])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("word, symbol, answer", [
    ("Hello", "H", True), ("Nice to meet you", "o", True),
    ("123456", "5", True), ("Hi!", "!", True),
    ("Cool", "c", True)])
def test_contains_positive(word, symbol, answer):
    ans = string_utils.contains(word, symbol)
    assert ans == answer


@pytest.mark.positive
@pytest.mark.parametrize("word, symbol, string", [
    ("Line", "i", "Lne"), ("How are you", "e", "How ar you"),
    ("547", "4", "57"), ("Awesome!!!", "!", "Awesome"),
    ("Range", "ange", "R"), ("Moon", "O", "Mn")])
def test_delete_symbol_positive(word, symbol, string):
    ans = string_utils.delete_symbol(word, symbol)
    assert ans == string


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"), ("!!", "!!"), ("", ""),
    ("   ", "   ")])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""), ("  ", " ")])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("word, symbol, answer", [
    (" ", " ", True), ("", "", True),
    ("cool", "с", False)])  # в последнем примере изменен язык
def test_contains_negative(word, symbol, answer):
    answ = string_utils.contains(word, symbol)
    assert answ == answer


@pytest.mark.negative
@pytest.mark.parametrize("word, symbol, string", [
    ("Line ", " ", "Line"),
    ("", "", ""), ("  ", " ", ""),
    ("Hello World", " ", "HelloWorld")])
def test_delete_symbol_negative(word, symbol, string):

    answ = string_utils.delete_symbol(word, symbol)
    assert answ == string
