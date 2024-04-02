def main():
    # expr = "3 + 4 * 2 / ( 1 - 5 )"
    expr = input("Enter expression: ")
    parsed_expr = infix_to_rpn(expr)
    # print(parsed_expr)
    print(f"= {compute_rpn(parsed_expr)}")


def infix_to_rpn(infix_expr: str, debug: bool = False) -> list[str]:
    queue = []
    stack = []
    number = ""

    for c in infix_expr:
        if not valid_token(c):
            raise ValueError(f"Invalid token '{c}'.")

        if c.isdigit():
            number += c
        elif number:
            queue.append(number)
            number = ""

        if c in "*/+-" or c == "(":
            if stack and precedence(c) == precedence(stack[-1]):
                queue.append(stack.pop())
            stack.append(c)
        elif c == ")":
            while (o := stack.pop()) != "(":
                queue.append(o)

        if debug and not c.isspace():
            print(f"token={c}\n{queue=}\n{stack=}\n")

    queue.append(number)
    while stack:
        queue.append(stack.pop())

    return queue


def compute_rpn(rpn_expr: list, debug: bool = False) -> str:
    q = []

    for tk in rpn_expr:
        if tk.isdigit():
            q.append(float(tk))
        else:
            r = q.pop()
            l = q.pop()
            match tk:
                case "*":
                    q.append(l * r)
                case "/":
                    q.append(l / r)
                case "+":
                    q.append(l + r)
                case "-":
                    q.append(l - r)
                case _:
                    raise ValueError("Invalid token")

        if debug:
            print(f"{tk=}, {q=}")

    return q.pop()


def valid_token(c: str) -> bool:
    return c.isdigit() or c in "*/+-()^ "


def precedence(op: str) -> int:
    if op == "^":
        return 4
    elif op in "*/":
        return 3
    elif op in "+-":
        return 2
    else:
        return -1


if __name__ == "__main__":
    main()
