def sumZero(self, n: int) -> List[int]:
        output = []
        if n%2==1:
            output.append(0)
            upper_ = int((n-1)/2)
        else:
            upper_ = int(n/2)
        for i in range(upper_):
            output.append(i+1)
            output.append(-i-1)
       # output = output.sort()
        return output
