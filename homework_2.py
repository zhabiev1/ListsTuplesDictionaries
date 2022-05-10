import sys
import time


def something(x):
    if x <= 1:
        return (x)
    else:
        return (something(x - 1) + something(x - 2))


x = int(sys.argv[1])
datafile = open("tuwas.csv", "w")
for n in range(1, x):
    t1 = time.time()
    datafile.write(str(something(n)) + "\t")
    t2 = time.time()

    duration = t2 - t1
    duration = round(duration, 10)
    datafile.write(str(duration) + "\n")
datafile.close()