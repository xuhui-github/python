import random

some_exceptions = [ValueError, TypeError, IndexError, None]

try:
    choice = random.choice(some_exceptions)
    print("raising {}".format(choice))
    if choice:
        raise choice("An error")
except ValueError:
    print("catch an ValueError")
except TypeError:
    print("catch a TypeError")
except Exception as e:
    print("catch some other error: %s" % (e.__class__.__name__))
else:
    print("this code called if there is no exception")
finally:
    print("this cleaning code is always called")
