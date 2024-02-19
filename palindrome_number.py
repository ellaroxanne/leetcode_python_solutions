class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_length = len(str(x))
        for i in range(str_length//2 + str_length % 2):
            if str(x)[i] != str(x)[-1 * i - 1]:
                return False
        return True
