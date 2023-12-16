class MyClass:
    def smeth():
        print('This is a static method')
    #smeth = staticmethod(smeth)

    def cmeth(cls):
        print('This is a class method of',cls)
    cmeth=classmethod(cmeth)

class Rectangle:
    def __init__(self):
        self.width=0
        self.height=0

    def __setattr__(self,name,value):
        if name == 'size':
            self.width,self.height=value
        else:
            self.__dict__[name]=value

    def __getattr__(self,name):
        if name == 'size':
            return self.width, self.height
        else:
            raise AttributeError()


if __name__ == '__main__':
    MyClass.smeth()
    MyClass.cmeth()
    
    r=Rectangle()
    print(r.size)
    r.size=(200,300)
    print(r.width,r.height)
    r.color='pink'
    print(r.color)
    print(r.__dict__)

