a = ['you', 'are', 'beautiful']
maxx = len(a[0])
temp = a[0]
for i in a:
    if (len(i) > maxx):
        maxx = len(i)
        temp = i
print('the longest word is', temp)
print('length of word is', maxx)
