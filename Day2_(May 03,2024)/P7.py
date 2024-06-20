ip="is2 sentence4 This1 a3"
s=ip.split()
re=[0]*len(a)
for i in a:
    re[int(i[-1])-1] = i[::-1]
return ''.join(re)


