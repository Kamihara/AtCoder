str_n = input()
int_n = int(str_n)
count = 0
end = 10 ** (len(str_n) // 2)
for i in range(1, end + 1):
    if int(str(i) + str(i)) <= int_n:
        count += 1
print(count)
