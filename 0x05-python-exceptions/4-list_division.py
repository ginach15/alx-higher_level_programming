#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newlist = []

    for i in range(0, list_length):
        num = 0

        try:
            num = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("{}".format("division by 0"))
        except TypeError:
            print("{}".format("wrong type"))
        except IndexError:
            print("{}".format("out of range"))
        finally:
            newlist.append(num)
    return newlist
