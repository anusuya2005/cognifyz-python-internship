file=open("sample.txt",'r')
content=file.read()
text=content.split()
word={}
for w in text:
    if w in word:
        word[w] += 1
    else:
        word[w] = 1
for w in sorted(word):
    print(w,":",word[w])
file.close()
        


