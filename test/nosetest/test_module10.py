from nose.tools import timed

import time


@timed(0.3)
def test_case01():
    time.sleep(0.2)
