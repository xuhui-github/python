# __len__(self)
# __getitem__(self,key)
# __setitem__(self,key,value)
# __delitem__(self,key)


def check_index(key):
    """
    Is the given key an acceptable index?

    to be acceptable,the key should b a non-negative integer. if it
    is not an integer,a TypeError is raised;if it is negative,an
    IndexError is raised (since the sequence is of infinite length).
    """
    if not isinstance(key, int):
        raise TypeError
    if key < 0:
        raise IndexError


class ArithemeticSequence:
    def __init__(self, start, step=1):
        """
        start  - the first value in the sequence
        step   - the difference between two adjacent values
        changed  - a dictionary of values that have been modified by the user
        """
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, key):
        """
        Get an item from the arithmetic sequence.
        """
        check_index(key)

        try:
            return self.changed[key]
        except KeyError:
            return self.start + key * self.step

    def __setitem__(self, key, value):
        """
        change an item in the arithmetic sequence.
        """
        check_index(key)
        self.changed[key] = value

    def __delitem__(self, key):

        if self.changed[key]:
            del self.changed[key]


if __name__ == "__main__":
    s = ArithemeticSequence(1, 2)
    print("s[4] is %d\n" % s[4])
    s[4] = 2
    print("s[4]=2")
    print("s[4] is %d\n" % s[4])
    print("s[5] is %d\n" % s[5])
    del s[4]
    print("del s[4]")
    print("s[4] is now %d\n" % s[4])
