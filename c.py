s = '0: 480x640 1 30, '


print(s)
print(s[:-2])
print(s[:-2].split(' '))
print(s[:-2].split(' ')[1])
print(s[:-2].split(' ')[3][:-1])
kl = s[:-2].split(' ')[3][:-1]
if kl == '3':
    speed = 10
    #print the speed variabel
    print(speed)

# print(s[:-2].split(' ')[1][:-1].split('_'))
# print(s[:-2].split(' ')[1][:-1].split('_')[1])
# print(s[:-2].split(' ')[1][:-1].split('_')[1])
# print(s[:-2].split(' ')[1][:-1].split('_')[1].split('x'))
# print(s[:-2].split(' ')[1][:-1].split('_')[1].split('x')[0])
# print(s[:-2].split(' ')[1][:-1].split('_')[1].split('x')[1])
