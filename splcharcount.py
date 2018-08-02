s=input()
count=0
for i in s:
    if(i.isdigit() or i.isalpha()):
        i=s.isdigit()
        count=count+1
x=len(s)
print(x-count)