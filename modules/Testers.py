class tester:

    def __init__(self,start):
        self.state=start

    def nested(self,label):
        print(label,self.state)
        self.state += 1

F = tester(0)
F.nested("abc")
F.nested('def')
G = tester(42)
G.nested('abc')
G.nested('def')

class tester1:
    def __init__(self,start):
        self.state = start

    def __call__(self,label):
        print(label,self.state)

        self.state += 1 

H = tester1(99)
H('juice')
H('pancakes')

