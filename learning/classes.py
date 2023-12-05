class Super:
    def method(self):
        print('in Super.method')

class Sub(Super):
    def method(self):
        print('starting Sub.method')
        Super.method(self)
        print('ending Sub.method')


if __name__ == '__main__':
    x = Super()
    x.method()
    x = Sub()
    x.method()


