" FUALT WIRING AND BULBS PROGRAM "

class Solution:
    def countFlips(self, A):
        switch_pres = 0
        curr_state = 0
        for bulb in A:
            if bulb == curr_state:
                switch_pres += 1
                curr_state = 1 - curr_state
        
        return switch_pres

s = Solution()
print(s.countFlips([1,0,0,1,1,0,0,1]))