def buildArray(target, n):
    """
    :type target: List[int]
    :type n: int
    :rtype: List[str]
    """
    operationsArr = []
    pos = 0

    for num in range(1, n + 1):
        if pos >= len(target):
            break

        operationsArr.append("Push")

        if target[pos] != num:
            operationsArr.append("Pop")

        if target[pos] == num:
            pos += 1

    return operationsArr


def main():
    target = [1, 3]
    n = 3

    print(buildArray(target, n))


if __name__ == "__main__":
    main()
