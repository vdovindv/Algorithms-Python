class Solution:
    def maxDiff(self, num: int) -> int:
        a = str(num)
        b = str(num)
        
        for i in range(len(a)):
            if a[i] != '9':
                a = a.replace(a[i], '9')
                break
        
        if b[0] != '1':
            b = b.replace(b[0], '1')
        else:
            for i in range(1, len(b)):
                if b[i] != '0' and b[i] != b[0]:
                    b = b.replace(b[i], '0')
                    break
        return int(a) - int(b)
