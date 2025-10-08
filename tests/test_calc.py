import pytest

from src.rpn_parce import rpn_parce


def test_base_operatinons():
    assert rpn_parce('3 2 +') == 5.0
    assert rpn_parce('5 2 -') == 3.0
    assert rpn_parce('7 2 *') == 14.0
    assert rpn_parce('3 3 **') == 27.0


def test_operations_with_brackets():
    assert rpn_parce('( 8 ( 3 2 + ) - ) 4 *') == 12.0
    assert rpn_parce('( 3 4 + ) ( 5 2 - ) *') == 21.0


def test_operations_with_brackets_and_unary():
    assert rpn_parce('( ~ 5 4 + )') == -1.0
    assert rpn_parce('~ ( 5 4 * )') == -20.0


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        rpn_parce('3 0 /')
    with pytest.raises(ZeroDivisionError):
        rpn_parce('3 0 //')


def test_not_int_division():
    with pytest.raises(ValueError):
        rpn_parce('3.2 2 %')
    with pytest.raises(ValueError):
        rpn_parce('3.2 2 //')


def test_incorrect_expression():
    with pytest.raises(ValueError):
        rpn_parce('( 1 2')
    with pytest.raises(ValueError):
        rpn_parce('3 4 )')

def test_incorrect_subexpression():
    with pytest.raises(ValueError):
        rpn_parce('1 ( 1 2 ) +')
    with pytest.raises(ValueError):
        rpn_parce('( 2 ( 4 5 4 + - 4 ) * )')

def test_unknown_symbol():
    with pytest.raises(ValueError):
        rpn_parce('1 3 e')
    with pytest.raises(ValueError):
        rpn_parce('Efefg 1 2 +')

def test_not_enough_symbol_after_unary_sign():
    with pytest.raises(ValueError):
        rpn_parce('4 2 + ~')

def test_incorrect_symbol_after_unary_sign():
    with pytest.raises(ValueError):
        rpn_parce('~ e 2 4 -')

def test_not_enough_symbols_for_operation():
    with pytest.raises(ValueError):
        rpn_parce('2 3 4 + - -')
    with pytest.raises(ValueError):
        rpn_parce('1 +')
