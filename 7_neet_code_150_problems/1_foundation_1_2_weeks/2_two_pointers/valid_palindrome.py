class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([x for x in list(s) if x.isalnum()])
        i, j = 0, len(s) - 1
        print(s)
        while i < j:
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True



s = Solution()
str_ = "Was it a car or a cat I saw?"
print(s.isPalindrome(str_))