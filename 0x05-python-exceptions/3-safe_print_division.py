
#!/usr/bin/python3
# 3-safe_print_division.py


def safe_print_division(a, b):
    """return a/b."""
    try:
        res = a / b
    except (TypeError, ZeroDivisionError):
        res = None
    finally:
        print("Inside result: {}".format(res))
    return (res)
