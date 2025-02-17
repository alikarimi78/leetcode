class Solution1:
    def is_palindrome(self, x: int) -> bool:
        if x < 0:
            return False

        x = str(x)

        if len(x) < 2:
            return True

        revers_number_list = []

        for i in range(len(x)):
            revers_number_list.append(x[len(x) - 1 - i])

        revers_number = "".join(revers_number_list)

        if revers_number == x:
            return True
        else:
            return False


print(Solution1().is_palindrome(12321))


class Solution2:
    def is_palindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False


print(Solution2().is_palindrome(12321))
