fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print("there is no file with this name")
    quit()

for letter in fh:
    letter = letter.rstrip()
     print(letter.upper())
