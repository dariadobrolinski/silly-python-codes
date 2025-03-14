import sys

def tree(height):
    length = height * 2 - 1
    stars = 1
    for i in range(1, height):
        print(("*" * stars).center(length))
        stars += 2
    print("*".center(length))

# call tree on any number, ex: tree(10)
