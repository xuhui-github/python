class CounterList(list):
    def __init__(self,*args):
        super().__init__(*args) #call super contructor
        self.count=0

    def __getitem__(self,index):
        self.count+=1
        return super(CounterList,self).__getitem__(index)


if __name__ == '__main__':
    cl=CounterList(range(10))
    cl.reverse()
    print(cl)
    del cl[3:6]
    cl[1]+cl[4]
    print(cl[3])
    print(cl.count)
