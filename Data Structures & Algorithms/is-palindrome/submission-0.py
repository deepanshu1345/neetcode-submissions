class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = "".join(char for char in s if char.isalnum()).lower()
        reversed_text = text[::-1]
        return reversed_text == text