class MyError(Exception): pass

def stuff(file):
    raise MyError()

file=open('data','w')
try:
    stuff(file)
except MyError:
    print("got MyError")
finally:
    print("close file data")
    file.close()
    print("closed file data")
    try:
        pass
    except MyError:
        print("got MyError")

print("got not reached")
