from src.rpn_parce import rpn_parce


def main() -> None:
    e = input("Введите выражение в постфиксной польской нотации: ")

    res = rpn_parce(e)

    print(res)

if __name__ == "__main__":
    main()
