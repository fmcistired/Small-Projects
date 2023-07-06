# How to put strings together

# series = "Breaking Bad"
#
# print("check out " + series)
# print("check out {}".format(series))
# print(f"check out {series}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
series_character = input("Character from series ")

madlib = f"This tv show is so {adj}! It makes me want to {verb1}. " \
         f"Check it out and stay {verb2} as if you are {series_character}!"

print(madlib)