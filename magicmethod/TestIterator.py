class TestIterator:
    value=0
    def __next__(self): #return iterator value
        self.value+=1
        if self.value>10: raise StopIteration
        return self.value

    def __iter__(self): #return iterator object
        return self


if __name__ == '__main__':
    it = TestIterator()
    for val in it:
        print(val)
    print(list(TestIterator()))


