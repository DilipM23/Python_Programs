fname = input("Enter the file name :")
f = open(fname,"r")
line = int(input("Enter the number of lines to be displayed"))
for x in range(line) :
    data = f.readline()
    print(x+1, " : ", data)
f.seek(0)
wrdcnt = 0
word = input("Enter the word to be searched")
for line in f :
    r = line.split()
    wrdcnt += r.count(word)
f.close()
print(word, " appears ", wrdcnt, " times ")
