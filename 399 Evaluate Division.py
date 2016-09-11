equations = [["a","b"],["c","d"]]
values = [1,1]
query = [["a","c"],["b","d"],["b","a"],["d","c"]]

dic = {}
dic2 = {}
i = 0
reiteration = []
for eq in equations:
    if eq[0] not in dic and eq[1] not in dic:
        dic[eq[1]]= 1.0
        dic[eq[0]]= values[i]*1.0
        dic2[eq[1]] = eq[0]
        dic2[eq[0]] = eq[1]
    elif eq[0] in dic and eq[1] not in dic:
        dic[eq[1]]=dic[eq[0]]/values[i]
    elif eq[0] not in dic and eq[1] in dic:
        dic[eq[0]]=dic[eq[1]]*values[i]
    elif eq[0] in dic and eq[1] in dic:
        if dic[eq[0]]/dic[eq[1]]!=values[i]:
            if dic[eq[0]]==1.0:
                dic[eq[0]] = dic[eq[1]]*values[i]
                reiteration.append(eq[0])
            if dic[eq[1]]==1.0:
                dic[eq[1]] = dic[eq[0]]/values[i]
                reiteration.append(eq[1])
    i+=1

i=0

for eq in equations:
    if eq[0] in reiteration:
        dic[eq[1]] = dic[eq[0]]/values[i]
    if eq[1] in reiteration:
        dic[eq[0]] = values[i]*dic[eq[1]]
    i+=1
    
solution = []
print dic["c"],dic["d"]
for q in query:
    if q[0] not in dic or q[1] not in dic:
        solution.append(-1.0)
    elif (q[0] in dic2 or q[1] in dic2):
        if q[0] in dic2 and dic2[q[0]]!=q[1]:
            solution.append(-1.0)
        elif q[1] in dic2 and dic2[q[1]]!=q[0]:
            solution.append(-1.0)
        else:
            solution.append(dic[q[0]]/dic[q[1]])
    else:
        solution.append(dic[q[0]]/dic[q[1]])
    
print solution
