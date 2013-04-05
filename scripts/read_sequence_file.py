import sys
import screed

filename = sys.argv[1]
print(filename)

n = 0
for record in screed.open(filename):
    while n < 10:
        print(record['sequence'])
        n += 1
        break
