def char_vowel(char):
    vowels = ('a', 'e', 'i', 'o', 'u')
    if char not in vowels:
        return False
    return True


if __name__ == "__main__":
    print char_vowel(1)
    print char_vowel('a')
    print char_vowel('i')
    print char_vowel(2)
    print char_vowel('e')
