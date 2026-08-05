class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        acc = []

        for token in tokens:

            if bool(re.match(r"^-?\d+$", token)):
                acc.append(int(token))
            else:
                b = acc.pop()
                a = acc.pop()

                if token == "/":
                    num = int(a / b)
                else:
                    num = eval(f"{a}{token}{b}")

                acc.append(num)

        return acc[-1]