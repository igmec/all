def collatz(number):
    if number%2 == 0:
        print(str(number//2))
        return number//2

    else:
        print(str((number*3)+1))
        return (number*3)+1


try:
    print("Enter a number: ")
    num = int(input())

    while num != 1:
        num = collatz(num)

except ValueError:
    print("Not a valid number")


