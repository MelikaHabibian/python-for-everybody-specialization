name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
emails = list()
counts = dict()
for line in handle:
    if line.startswith("From:"):
        words = line.split()
        emails.append(words[1])
for email in emails:
    counts[email] = counts.get(email, 0) + 1
maxcount = None
maxemail = None
for email,count in counts.items():
    if maxcount is None or count > maxcount:
        maxcount = count
        maxemail = email
print(maxemail, maxcount)
