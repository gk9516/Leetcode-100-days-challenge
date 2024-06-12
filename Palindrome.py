class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            print("false")
        str_x = str(x)
        reversed_str_x = str_x[::-1]
        result = str_x == reversed_str_x
        if result==1:
            print("true")
        else:
            print("false")
