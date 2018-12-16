n = map(int, input().split())
a_str_list = list(input().split())

a_int_list = [int(s) for s in a_str_list]

#print(a_str_list)
#print(sorted(a_int_list, reverse=True))

end_f = False
cnt = 0

while end_f == False:
    a_new_list = []
    f = False
    cnt = cnt + 1
    for a in sorted(a_int_list, reverse=True):
        if a % 2 == 0 and f == False:
            a_new_list.append(a/2)
            f = True
        else:
            a_new_list.append(a*3)
    #print(a_new_list)
    a_int_list = a_new_list

    if f == False:
        end_f = True

print(cnt-1)