def factorial(n):
    """caclualting n factorial recuresively"""
    if n<=1:
        return 1
    else:
       # print (n/0)
        return n *factorial(n-1)

try:
    factorial(1000)
except RecursionError:
    print("This program cannot calculalte factorials of higher values")
except OverflowError:
    print("we are doing a divison b zero ")
# except (RecursionError,ZeroDivisionError):
#     print("we are doing a divison b zero ")