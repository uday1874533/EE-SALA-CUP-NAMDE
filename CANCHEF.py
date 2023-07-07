# cook your dish here
# DAY1

for tc in range(int(input(" "))):
    x,y=map(int,(input().split(" ")))
    if x*15>=y*2:
        print("Yes")
    else:
        print("No")
