def computepay(h,r):
    if h > 40 :
        pay = (40 * r) + (h - 40) * (1.5 * r)
        return pay
    else :
        pay = h * r
        return pay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")

try:
    hr = float(hrs)
    rt = float(rate)
except:
    print("Please enter a valid number")
    quit()

p = computepay(hr,rt)
print("Pay",p)
