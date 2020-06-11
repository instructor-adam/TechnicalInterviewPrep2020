filepath = 'tri.txt'
triangle = []
with open(filepath) as fp:
   line = fp.readline()
   triangle.append(line)
   cnt = 1
   while line:
    line = "Line {}: {}".format(cnt, line.strip())
    line = fp.readline()
    #line = "Line {}: {}".format(cnt, line.strip())
    cnt+=1
    triangle.append(line)


for e in triangle:
    e = [x for x in range(len(e)) if x != '\n']
lst = []
for m in triangle:
    lst.append(list(m.split(' ')))

#print("max", max(lst[0]))
res = []


for e in lst:
    #print(max(e))
    e = [x for x in range(len(e)) if x != '\n']
    res.append(int(float(max(e))))

num = sum(res)
print(num)

