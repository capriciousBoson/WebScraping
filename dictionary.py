T = int(input())

results=[]

for i in range(T):
    inputline2 = input().split(' ')
    R = int(inputline2[0])
    C = int(inputline2[1])
    H = int(inputline2[2])
    V = int(inputline2[3])
    res='POSSIBLE'
    rows = []
    cols =[]
    j=0
    for i in range(R):
        rows.append(input())
    for C in range(C):
        colstrng=''
        for items in rows:
            colstrng=colstrng+items[j]
        cols.append(colstrng)
        j+=1
    for items in rows:
        if items.count('@') >= V+1:




     results.append(res)

for i in range(T):
    print('Case #{}: {}'.format(i+1,results[i]))
