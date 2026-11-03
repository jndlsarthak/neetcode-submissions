class Solution:
    def countBits(self, n: int) -> List[int]:
        list1 = [0]
        for i in range(1,n+1): 
            b = str(bin(i))
            x = 0
            for j in range(len(b)):
                if b[j] == '1':
                    x +=1
            list1.append(x)
        return list1

        # list1 = [0]
        # for i in range(1, n + 1):
        #     list1.append(bin(i).count('1'))
        # return list1