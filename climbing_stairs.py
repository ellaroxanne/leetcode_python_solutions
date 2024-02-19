class Solution:
    time_dict = {1: 1, 2: 2}
    def climbStairs(self, n: int) -> int:
        if n in self.time_dict.keys():
            return self.time_dict[n]
        else:
            self.time_dict[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.time_dict[n]
        
