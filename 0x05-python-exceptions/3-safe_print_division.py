#!/usr/bin/python3

def afe_print_division(a, b):
    """Returns the division of a by b"""
    try:
        div = a/b
    except(TypeErroe, ZeroDivisionError):
        div = None
    finally:
        print("inside result: {}".format(div))
return(div)
