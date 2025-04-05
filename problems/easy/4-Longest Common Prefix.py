from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        output_list = []
        output_list_temp = []
        def check_existence(first_word_: str, word_: str) -> list[str]:
            letter_count_first_word = len(first_word_)
            for i in range(letter_count_first_word):
                if first_word_[i] in word_:
                    output_list_temp.append(first_word_[i])
                    if len(output_list_temp) > 0:
                        if output_list_temp[i+1] == word_:

            return output_list

        first_word = strs.pop()
        for word in strs:
            out_put_list = check_existence(first_word, word)
            if






