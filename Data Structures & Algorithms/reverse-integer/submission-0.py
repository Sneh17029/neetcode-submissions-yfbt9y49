class Solution:
    def reverse(self, x: int) -> int:
        f = 0
        if x < 0:
            f = 1
        x = x if x > 0 else (-1*x)
        rev = 0
        while x:
            rev = rev*10 + x%10
            x = x//10
        rev = rev if f == 0 else (-1*rev)
        if rev < -2147483648 or rev > 2147483647:
            return 0
        return rev