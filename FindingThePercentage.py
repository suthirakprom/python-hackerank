myDict = {}
n = int(input())
for i in range(n):
    arr = input().split()
    myDict[arr.pop(0)] = map(int, arr)
name = input()
print(("{:.2f}".format(sum(myDict[name])/3)))