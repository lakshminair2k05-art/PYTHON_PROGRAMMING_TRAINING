
class Solution(object):
    def climbingStairs(n):
        if n==1 or n==0:#basecase
            return 1
        return climbingStairs(n-1)+climbingStairs(n-2)#recursive case
    #call func
    print(climbingStairs(4))