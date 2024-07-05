class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans=numBottles
        while numBottles>=numExchange:
            val=numBottles/numExchange
            rem=numBottles%numExchange
            ans+=val
            numBottles=val+rem
        return int(ans)
