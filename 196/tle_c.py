n = int(input())
count = 0
for i in range(n+1):
    str_i = str(i)
    len_i = len(str_i)
    if len_i % 2 != 0:
        continue
    first_harf = str_i[0:len_i//2] 
    latter_harf = str_i[len_i//2:]
    if first_harf == latter_harf:
        count += 1
print(count)