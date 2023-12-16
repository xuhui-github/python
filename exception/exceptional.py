def divide_with_exception(number, divisior):
    try:
        print("{} / {} = {}".format(
            number,divisior,number/divisior * 1.0))
    except ZeroDivisionError:
        print("You can't divide by zero")


