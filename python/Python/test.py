

final = ''
for i in range(len(queries)):
   p,q,r = queries[i][0],queries[i][1],queries[i][2]
   suum = r
   for j in range(p,q):
      suum = suum + j
   final = final + suum +' '
print(final)

