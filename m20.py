class DivisibleBySeven:
    def __init__(self, n):
        self.n = n

    def generate(self):
        for i in range(self.n):
            if i % 7 == 0:
                yield i
