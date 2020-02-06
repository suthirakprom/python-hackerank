arr = []
for i in range(int(input())):           # loop the input of how many times the user input
    s = input().split()                 # take input from the user put it in s separate per input by a space
    for i in range(1,len(s)):           # the len of s is count by the soc
        s[i] = int(s[i])        
    if s[0] == "append":
        arr.append(s[1])
    elif s[0] == "extend":    
        arr.extend(s[1:])
    elif s[0] == "insert":
        arr.insert(s[1],s[2])
    elif s[0] == "remove":
        arr.remove(s[1])
    elif s[0] == "pop":
        arr.pop()
    elif s[0] == "sort":
        arr.sort()
    elif s[0] == "reverse":
        arr.reverse()
    elif s[0] == "print":
        print(arr)