# Kristen Anderson
# CIS261
# Iteration and Recursive Functionaility

def factorialRecursive(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorialRecursive(number - 1)

def factorialIterative(number):
    factor = 1
    for number in range(2, number+1):
        factor = number * factor
    return factor
 
def main():
    print ("Factorial results using an interative function")
    print("0! =", factorialIterative(0))
    print("5! =", factorialIterative(5))
    print("10! =", factorialIterative(10))
    print("25! =", factorialIterative(25))
    print("50! =", factorialIterative(50))
    print("100! =", factorialIterative(100))
    print()
    print ("Factorial results using a recursive function")
    print("0! =", factorialRecursive(0))
    print("5! =", factorialRecursive(5))
    print("10! =", factorialRecursive(10))
    print("25! =", factorialRecursive(25))
    print("50! =", factorialRecursive(50))
    print("100! =", factorialRecursive(100))

if __name__ == "__main__":
    main()

