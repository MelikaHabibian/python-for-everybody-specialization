hrs = input("Enter Hours:")
rate = input("Enter Rate:")

try:
    h = float(hrs)
    r = float(rate)
except:
    print("Please enter a valid number")
    quit()

pay = 0
if h > 40 :
    pay = (40 * r) + (h - 40) * (1.5 * r)
else :
    pay = h * r

print(pay)
