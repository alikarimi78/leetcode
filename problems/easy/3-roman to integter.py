class Solution1:
    def romanToInt(self, s: str) -> int:
        mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        answer = 0
        counter = len(s)
        i = 0

        while i < counter:
            if not i == len(s) - 1:
                if mapping[s[i]] < mapping[s[i + 1]]:
                    answer += mapping[s[i + 1]] - mapping[s[i]]
                    i += 1
                else:
                    answer += mapping[s[i]]

            else:
                answer += mapping[s[i]]
            i += 1
        return answer


print(Solution1().romanToInt("MCMXCIV"))


class Solution2:
    def romanToInt(self, s: str) -> int:
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        res = 0
        k = 0
        while k < len(s):
            if k+1<len(s) and roman_values[s[k+1]] > roman_values[s[k]]:
                res += roman_values[s[k+1]] - roman_values[s[k]]
                k += 1
            else:
                res += roman_values[s[k]]
            k+=1



        return res

print(Solution2().romanToInt("MCMXCIV"))
