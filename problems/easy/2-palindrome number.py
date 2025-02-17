class Solution1:
    def is_palindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        if len(x) < 2:
            return True
        revers_number_list = []
        for i in len(x):
            revers_number_list.insert(len(x) - 1 - i, x[i])
        print(revers_number_list)


print(Solution1().is_palindrome(123))