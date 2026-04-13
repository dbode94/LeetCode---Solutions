def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    valid_oper = set(['+', '-', '*', '/'])
    num_stack = []

    for value in tokens:
        if value not in valid_oper:
            num_stack.append(int(value))

        else:
            num2 = num_stack.pop()
            num1 = num_stack.pop()
            # ecuation = f"{num1}{value}{num2}"
            if value == "+":
                num_stack.append(num1 + num2)
            elif value == "-":
                num_stack.append(num1 - num2)
            elif value == "*":
                num_stack.append(num1 * num2)
            else:
                num_stack.append(int(num1 / float(num2)))

    return num_stack[0]


def main():
    tokens = ["10", "6", "9", "3", "+", "-11",
              "*", "/", "*", "17", "+", "5", "+"]

    print(evalRPN(tokens))


if __name__ == "__main__":
    main()
