



s="lee(t(c)o)de)"
s=list(s)
stack=[]

for i , char in enumerate(s):
    if char =="(":
        stack.append(i)
    elif char==")":
        if stack:
            stack.pop()
        else:
            s[i]=""
while stack:
    s[stack.pop()]=""
print("".join(s))