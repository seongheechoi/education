# iter = range(3).__iter__()
#
# print(iter)
# print(iter.__next__())
# print(iter.__next__())
# print(iter.__next__())
# print(iter.__next__())

class CustomRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            rvalue = self.current
            self.current += 1
            return rvalue
        else:
            raise StopIteration

for i in CustomRange(1, 5):
    print(i)
