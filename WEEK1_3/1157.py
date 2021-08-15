n = input().upper()
n_list = list(set(n))
cnt_list = []

for i in n_list:
    cnt = n.count(i)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) >= 2:
    print("?")

else:
    print(n_list[cnt_list.index(max(cnt_list))].upper())