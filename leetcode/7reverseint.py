class Solution(object):
    def __init__(self, x:int):
        self.x = x
    def reverse(self):
        if -10<self.x<10:
            return self.x  
        else:
            str_x = str(self.x)
            if str_x[0] == '-':
                result = - int(str_x[1:][::-1])
            else:
                result = int(str_x[::-1])
            return result if -2**31<result<2**31 else 0

    def reverse_better(self):
        y, res = abs(self.x), 0
        # 则其数值范围为 [−2^31,  2^31 − 1]
        boundry = (1<<31) -1 if self.x>0 else 1<<31
        while y != 0:
            res = res*10 +y%10
            if res > boundry :
                return 0
            y //=10
        return res if self.x >0 else -res

if __name__=='__main__':
    from sys import getsizeof
    test= 213543123123
    test2 = str(test)
    print(getsizeof(test))
    print(getsizeof(test2))
    a = Solution(test)
    print(a.reverse_better())

