def palindrome(string):
    return string == string[::-1]

if __name__ == "__main__":
    print palindrome("radar")
    print palindrome("Kiran")
    print palindrome("Kumar")
    print palindrome("aabbaa")
    print palindrome("xyz")
