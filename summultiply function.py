def sum(arguments):
    total = 0
    for number in arguments:
        total += number
    return total

def multiply(arguments):
    total = 1
    for number in arguments:
        total = total * number
    return total

if __name__ == "__main__":
    print sum([1,2,3,4])
    print multiply([1,2,3,4])

