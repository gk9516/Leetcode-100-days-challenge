import sys
sys.set_int_max_str_digits(0)
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        lk=[str(i) for i in num]
        ch=int("".join(lk))
        total=str(ch+k)
        l=[int(i) for i in total]
        return l
