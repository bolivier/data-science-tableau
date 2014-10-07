line = True
cols = []
while 1:
    s = set()
    line = raw_input()
    while line != '.':
        s.add(line)
        line = raw_input()
    if s:
        cols.append(s)
    else:
        break

print cols
intersect = set.intersection(*cols)
for s in intersect:
    print s+','
print "Need to remove"
for s in sorted(list(cols[-1].difference(intersect))):
    print s

