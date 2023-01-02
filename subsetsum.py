test_cases = [[[3, 4, 5, 5, 5], [3, 5, 6, 8], False],
              [[3, 4, 5, 5, 5, 5], [5, 5, 8, 9], True],
              [[3, 4, 5, 5, 5], [3, 5, 5, 9], True],
              [[3, 4, 5, 5, 5, 5], [5, 6, 8, 8], False],
              [[3, 4, 5, 5, 5], [3, 5, 6, 8], False]]

# [3, 4, 5, 5], [ 8, 9]


def space_satisfies(noodles, spaces) -> bool:
    noodles.sort()
    spaces.sort()

    # print(noodles, spaces)

    while spaces:
        if spaces[0] > 10:
            return True
        elif spaces[0] in noodles:
            noodles.remove(spaces[0])
            spaces.pop(0)
        elif spaces[0] - noodles[0] in noodles:
            noodles.remove(spaces[0] - noodles[0])
            noodles.remove(noodles[0])
            spaces.pop(0)
        else:
            return False

    return True


if __name__ == '__main__':
    for noodles, space, answer in test_cases:
        print(noodles, space, answer)
        print("Pass" if space_satisfies(noodles, space) == answer else "Fail")
        print()
