class Bird:
    def __init__(self):
        print("Bird.__init__")
        self.hungry=True

    def eat(self):
        if self.hungry:
            print("Ahhh ... Hungry")
            self.hungry=False
        else:
            print('No thanks')

class SongBird(Bird):
    def __init__(self):
        #Bird.__init__(self)
        super().__init__()
        self.sound='Squawk'
    def sing(self):
        print(self.sound)


if __name__ == '__main__':
    b=Bird()
    b.eat()
    b.eat()
    print('--------------------')
    s=SongBird()
    s.sing()
    s.eat() #SongBird doesn't contain any initialzation code dealing with hungry attribute.the SongBird constructor must call the constructor of superclass 
    s.eat()
