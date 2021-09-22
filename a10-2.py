name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hours = list()
counts = dict()
for line in handle:
    words = line.split()
    if len(words) > 2 and words[0] == 'From':
        word = words[5]
        word = word.split(":")
        hours.append(word[0])
for hour in hours:
    counts[hour] = counts.get(hour, 0) + 1
for hour,count in sorted(counts.items()):
    print(hour, count)
