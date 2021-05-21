import csv
with open('winequality-red.csv', 'r') as f:
    wines = list(csv.reader(f, delimiter=';'))

print(wines[:3])

qualities = [float(item[-1]) for item in wines[1:]]
print(qualities)
print(sum(qualities) / len(qualities))