class NewRangeFunction:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.start<self.stop:
            raise StopIteration
        current_value = self.start
        self.start -= 1
        return current_value

range1 = NewRangeFunction(10,1)
list1 = []
for i in range1:
    list1.append(i)
print(list1)

