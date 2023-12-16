class Rectangle:
    def __init__(self):
        self.width=0
        self.height=0

    def set_size(self,size):
        self.width,self.height = size

    def get_size(self):
        return self.width,self.height
    size=property(get_size,set_size) #r.size can access


if __name__ == '__main__':
    r=Rectangle()
    r.width=10
    r.height=5
    print(r.get_size())
    r.set_size((100,50))
    print(r.width)
    print(r.size)
    r.size=200,300
    print(r.width)

