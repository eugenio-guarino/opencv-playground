f = open('counter.txt', 'rt+')
hello = f.readline()
number = int(hello)
f = open('counter.txt', 'w')
f.write('8')
print(number)
