def divide(n1,n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print(error)
        return False

print(divide(2,0))
