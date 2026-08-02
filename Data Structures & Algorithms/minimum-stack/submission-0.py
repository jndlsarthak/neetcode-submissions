class MinStack:

    def __init__(self):
        self.acc = []

    def push(self, val: int) -> None:
        self.acc.append(val)

    def pop(self) -> None:
        self.acc.pop()

    def top(self) -> int:
        return self.acc[-1]

    def getMin(self) -> int:
        temp = self.acc[0]
        for i in range(len(self.acc)) :
            temp = min(temp,self.acc[i])

        return temp
