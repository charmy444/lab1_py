from src.functions import both_is_int, is_num
from src.constants import UNARY_SYMBOLS, OPERATIONS, NUMS


def rpn_parce(tokens, start=0):
    if type(tokens) == str:
        tokens = tokens.split()
    stack = []
    i = start

    while i < len(tokens):
        token = tokens[i]

        if is_num(token):
            # Проверяем число ли это, кладем в стек
            stack.append(float(token))
            i += 1

        elif token == '(':
            # Вычисляем подвыражение внутри скобок
            result, new_i = rpn_parce(tokens, i + 1)
            stack.append(result)
            i = new_i

        elif token == ')':
            # Конец подвыражения
            if len(stack) != 1:
                raise ValueError('Некорректное подвыражение')
            return stack.pop(), i + 1

        elif token in OPERATIONS:
            # Производим какую-то из операций
            if len(stack) < 2:
                raise ValueError('Недостаточно символов для операции')
            b = stack.pop()
            a = stack.pop()
            match token:
                case '+':
                    stack.append(a + b)
                case '-':
                    stack.append(a - b)
                case '*':
                    stack.append(a * b)
                case '**':
                    stack.append(a ** b)
                case '%':
                    if both_is_int(a,b):
                        stack.append(a % b)
                    else:
                        raise ValueError('Операция возможна только с целыми числами')
                case '/':
                    try:
                        stack.append(a / b)
                    except ZeroDivisionError:
                        raise ZeroDivisionError('Невозможно делить на ноль')
                case '//':
                    if both_is_int(a,b):
                        try:
                            stack.append(a // b)
                        except ZeroDivisionError:
                            raise ZeroDivisionError('Невозможно делить на ноль')
                    else:
                        raise ValueError('Операция возможна только с целыми числами')
            i += 1


        elif token in UNARY_SYMBOLS:
            i += 1
            if i >= len(tokens):
                raise ValueError('Недостаточно символов после унарного знака')
            next_token = tokens[i]

            # Обрабатываем символ за унарным знаком
            if next_token in NUMS:
                operand = int(next_token)
            elif next_token == '(':
                operand, new_i = rpn_parce(tokens, i + 1)
                i = new_i - 1 # Изменяем индекс, чтобы продвинуться по циклу
            else:
                raise ValueError(f'Неверный символ после унарного знака')

            if token == '~':
                stack.append(-operand)
            elif token == '$':
                stack.append(operand)

            i += 1

        else:
            raise ValueError("Неизвестный символ")

    if len(stack) != 1:
        raise ValueError("Некорректное выражение")
    return stack.pop()
