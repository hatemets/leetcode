import re

class Solution:
    def isPalindrome(self, word: str) -> bool:
        if (len(word) < 2):
            return True

        cleaned_word: str = re.sub(r"(\W+|_)", "", word).lower()
        start, end = 0, len(cleaned_word) - 1

        while start < end:
            if cleaned_word[start] != cleaned_word[end]:
                return False
            start += 1
            end -= 1

        return True


sol: Solution = Solution()

# Palindromes
# print(sol.isPalindrome("hahahahah"))
# print(sol.isPalindrome(""))
# print(sol.isPalindrome("anna"))
# print(sol.isPalindrome("asdfgfdsa"))
# print(sol.isPalindrome("A man, a plan, a canal: Panama"))
print(sol.isPalindrome("ab_a"))


# Not palindromes
# print(sol.isPalindrome("jessejk"))
# print(sol.isPalindrome("kjesxxzsejk"))

