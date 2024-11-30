class Solution:
    def countFlips(self, A, N):
        # Initialize the number of switches pressed
        switches_pressed = 0
        
        # Variable to track the current state of the bulbs
        current_state = 0
        
        # Iterate through the array
        for bulb in A:
            # If the current bulb is in an off state (taking into account the flips made so far)
            if bulb == current_state:
                # Flip the state of the bulb and all bulbs to its right
                switches_pressed += 1
                # Toggle the current state (0 -> 1, 1 -> 0)
                current_state = 1 - current_state
        
        return switches_pressed

A = [1,0,0,1]
N = 4
sol = Solution()
print(sol.countFlips(A,N))