#  TO FIND FACTORIAL OF 4 = 4 !  4 * 3 * 2 * 1 = 24

# THE PROCESS OF FINDING A FACTORIAL ENDS AFTER WE ENCOUNTER NR. 1

# 1 IS THE BASE CONDITION

def factorial(number):
    """ A mathematical pattern for finding a factorial number"""

    if number==1: # <-- Base condition ,  whenever our program triggers it we can terminate our program.

        return 1

    else:

        return number*factorial(number-1)


result=factorial(4)

print(result)







