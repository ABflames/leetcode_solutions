class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        prefix = ""
        position = 0

        while position < len(strs[0]):
            character = strs[0][position]

            for word in strs:

                if position >= len(word):
                    return prefix

                if word[position] != character:
                    return prefix

            prefix += character
            position +=1

        return prefix