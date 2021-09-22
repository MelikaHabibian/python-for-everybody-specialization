fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        count = count + 1
        num = float(line[20:])
        total = total + num
avg = total / count
print("Average spam confidence: ", avg)
