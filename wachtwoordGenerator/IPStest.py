import time
now = time.time()

ctr = 0
while now + 1 > time.time():
    ctr += 1
print(ctr)

