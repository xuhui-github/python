import logging

module_logger = logging.getLogger("exampleApp.otherMod2")


def add(x, y):
    logger = logging.getLogger("exampleApp.otherMod2.add")
    # logger.info("add %s and %s to get %s" % (x, y, x+y))
    return x + y
