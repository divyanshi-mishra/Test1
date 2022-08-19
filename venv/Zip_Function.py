names= ("Aman", "Shriya", "Atul", "Shriya")
interest = ("Art", "Science", "Games", "Football")

zipped = list(zip(names,interest))
print(zipped)

zipped = set(zip(names,interest))
print(zipped)

zipped = dict(zip(names,interest))
print(zipped)

zipped = zip(names,interest)
print(zipped)

for (a,b) in zipped:
    print (a,b)