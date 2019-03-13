class Nint(int):
    def __rsub__(self, other):
        return int.__sub__(self, other)
