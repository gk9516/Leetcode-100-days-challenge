class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        f0=0
        f1=1
        sum=0
        for i in range(n):
            if i>=1:
                sum=f0+f1
                f0=f1
                f1=sum
        return sum
