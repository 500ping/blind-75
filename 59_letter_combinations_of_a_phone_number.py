from typing import List

PHONE_NUM_DICT = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}


def letterCombinations(digits: str) -> List[str]:
    res = []

    def helper(current, left_over_digits):
        if not left_over_digits:
            res.append(current)
        else:
            for char in PHONE_NUM_DICT[left_over_digits[0]]:
                helper(current + char, left_over_digits[1:])

    if digits:
        helper("", digits)

    return res


digits = "23"
print(letterCombinations(digits))