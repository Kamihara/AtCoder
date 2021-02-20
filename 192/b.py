s = input()
list_s = list(s)
flag = False

for i in range(len(list_s)):
    elm = list_s[i]
    if (i + 1) % 2 == 1:
        if not elm.islower():
            flag = True
            break
    else:
        if not elm.isupper():
            flag = True
            break

if flag == True:
    print('No')
else:
    print('Yes')