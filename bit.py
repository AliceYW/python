class BIT:
    def __init__(self, list):
        self.a = [0] + list
        for i in range(1, len(self.a)):
            self.add(i, list[i])

    def sum(self, i):
        result = 0
        i += 1
        while i:
            result += self.a[i]
            i -= i & -i
        return result

    def add(self, i, v):
        i += 1
        while i < len(self.a):
            self.a[i] += v
            i += i & -i

class BIT2:
    def __init__(self, n):
        self.a = [{i} for i in range(n+1)]
        self.a[0].pop()
        for i in range(1, len(n)):
