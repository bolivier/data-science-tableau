s = "INSERT INTO accident VALUES (1,10001,1,1,0,2,81,2340,15,1,2010,6,4,10,1,11,1,'I-85                          ','                              ',621,32.64106389,-85.35469167,0,42,0,0,1,1,4,0,3,1,0,1,0,'0000000',99,99,4,20,99,99,0,0,0,1,1);"

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

def processLine(s):
    if s.startswith("INSERT INTO accident VALUES"):
        i_PVH_INVL = find_nth(s, ',', 4)
        s = s[:i_PVH_INVL]+',0'+s[i_PVH_INVL:]
        i_PERNOTMVIT_and_PERMVIT = find_nth(s, ',', 6)
        s = s[:i_PERNOTMVIT_and_PERMVIT]+',0,0'+s[i_PERNOTMVIT_and_PERMVIT:]
        print s

line = raw_input()
while line:
    processLine(line)
    line = raw_input()

#processLine(s)
