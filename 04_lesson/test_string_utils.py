import pytest
from string_utils import StringUtils

utils = StringUtils()


@pytest.mark.parametrize("input_string, expected", [
        ("fтест", "Тест"),
        ("skypro", "Skypro"),
        ("hello world", "Hello world"),
    ])
def test_capitalize_positive(input_string, expected):
    assert utils.capitalize(input_string) == expected


@pytest.mark.parametrize("input_string, expected", [
    ("", ""),
    (" ", " "),
    ("123abc", "123abc"),
])
def test_capitalize_negative(input_string, expected):
    assert utils.capitalize(input_string) == expected


@pytest.mark.parametrize("input_string, expected", [
    ("skypro", "skypro"),
    ("skypro", "skypro"),
    ("   hello world", "hello world"),
])
def test_trim_positive(input_string, expected):
    assert utils.trim(input_string) == expected


@pytest.mark.parametrize("input_string", [
    "",
    " ",
    None,
    123,
])
def test_trim_negative(input_string):
    if input_string == "":
        assert utils.trim(input_string) == ""
    elif input_string == " ":
        assert utils.trim(input_string) == ""
    else:
        with pytest.raises((AttributeError, TypeError)):
            utils.trim(input_string)


@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("Skypro", "U", False),
    ("SkyPro", "yP", True),
])
def test_contains_positive(string, symbol, expected):
    assert utils.contains(string, symbol) == expected


@pytest.mark.parametrize("input_string, symbol, expected", [
    ("", "S", False),
    ("SkyPro", "", True),
    ("", "", True),
])
def test_contains_negative(input_string, symbol, expected):
    assert utils.contains(input_string, symbol) == expected


@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("Hello World", " ", "HelloWorld"),
])
def test_delete_symbol_positive(string, symbol, expected):
    assert utils.delete_symbol(string, symbol) == expected


@pytest.mark.parametrize("input_string, symbol, expected", [
    ("", "S", ""),
    ("SkyPro", "", "SkyPro"),
    ("   ", " ", ""),
])
def test_delete_symbol_negative(input_string, symbol, expected):
    assert utils.delete_symbol(input_string, symbol) == expected
