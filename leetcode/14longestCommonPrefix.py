class Solution(object):
    def __init__(self,strs:[str]):
        self.strs = strs
    
    def longestCommonPrefix(self):
        maxlen = min([len(x) for x in self.strs])
        commonstr = ''
        for i in range(0,maxlen):
            single_char = len(set([x[i] for x in self.strs]))
            if single_char == 1:
                commonstr += self.strs[0][i]
            else:
                break
        return commonstr

if __name__ == '__main__':
    test  = ["flower","flow","flight"]
    temp = Solution(test)
    answer = temp.longestCommonPrefix()
    print(answer)
    