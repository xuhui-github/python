import logging
import otherMod


def main():
    """
    The main entry point of the application
    """
    logging.basicConfig(filename="mySnake.log", level=logging.INFO)
    logging.info("Program started")
    result = otherMod.add(2, 5)
    logging.info("Done!")


if __name__ == "__main__":
    main()
