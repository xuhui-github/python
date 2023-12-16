def funny_division3(anumber):
    try:
        if anumber == 13:
            raise ValueError('13 is  an unlucky number')
        return 100/anumber
    except ZeroDivisionError:
        print("Enter a number other than zero")
    except TypeError:
        print("Enter a numerical number")
    except ValueError:
        print("No, No, not 13")
        raise

if __name__ == '__main__':
    funny_division3(13)


