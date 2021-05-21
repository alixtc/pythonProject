import random

globalstreak = 0

# search function
def strsearch(stri):
    counter = 0
    streak = 0
    curr_val = stri[0]
    for i in range(1, len(stri)):
        if stri[i] == curr_val:
            counter += 1
        else:
            curr_val = stri[i]
            counter = 0

        if counter == 6:
            streak += 1
            counter = 0
    return streak


# create a sequence
for i in range(10000):
    seq = random.choices(["T", "H"], k=100)
    if  strsearch(seq) > 0:
        globalstreak +=1

print("Percentage of draws with a 6 contiguous sequence")
print(globalstreak / 100)
