word = input()
c_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in c_list:
    word = word.replace(i, "*")

print(len(word))