'''
This program prompt a user for a height of a pyramid and build one using the
hashtag symbol.
---Program written by Son Nguyen---
'''

def promtUser():
    valid = False
    while not(valid):
        try:
            user_input = int(input("Enter a pyramid height: "))
            if user_input <= 0 or user_input > 23:
                print("Please enter a positive value less than or equal than 23")
            else:
                valid = True
                return user_input
        except:
            print("Please enter an integer value")

def makePyramid (height):
    for i in range(pyramid_height):
        space_length = pyramid_height - i - 1
        space = " " * space_length
        hashtag = "#" * (pyramid_height - space_length)
        print(space + hashtag + " " + hashtag + space)

pyramid_height = promtUser()
makePyramid(pyramid_height)

