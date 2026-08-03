class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = []
        for i in range(len(temperatures)-1):
            temp = 0
            for j in range(i+1,len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    temp = j - i
                    break
                else:
                    temp +=0
            l.append(temp)
        l.append(0)
        return l

        