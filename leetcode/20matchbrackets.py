class Solution(object):
    def __init__(self,s:str):
        self.s = s
    
    def isValid(self):
        dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in self.s:
            if c in dic: stack.append(c)
            elif dic[stack.pop()] != c: return False 
        return len(stack) == 1




if __name__ == '__main__':
    test = ('[({(())}[()])]')
    a = Solution(test)
    print(a.isValid())