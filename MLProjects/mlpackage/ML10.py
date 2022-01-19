count=1
while(count<=5):
    print(count,end="\t")
    count=count+1
count=1
print()
while(True):
    print("count=",count)
    count=count+1
    if(count==4):
        break

for ch in "Kanpur":
    print("Hello= ",ch)

words=["India","japan","usa"]
for w in words:
    print(w," ",len(w))