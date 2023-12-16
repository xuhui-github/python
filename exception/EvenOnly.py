class EvenOnly(list):
    def append(self,integer):
        if not isinstance(integer,int):
            raise TypeError('Only integer can be appended')

        if integer%2:
            raise ValueError('Only even number can be appended')

        super().append(integer)

if __name__ == '__main__':
    lst=EvenOnly()
    try:
        lst.append(1);
        lst.append(3);
        lst.append(4);
    except Exception as e:
        print(e)
        try:
            lst.append('last')

        except Exception as e:
            print(e)
        
