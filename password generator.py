from random import randint

def create_random_chars(charCount):
    return "".join(chr(randint(33,126)) for i in range(charCount))


print(create_random_chars(10))
