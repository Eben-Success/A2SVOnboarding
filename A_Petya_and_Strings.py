
s1 = input()
s2 = input()


#If the first string is less than the second one, print "-1". 
# If the second string is less than the first one, print "1". 
# If the strings are equal, print "0". Note that the letters'
# case is not taken into consideration when the strings are compared.

l = 0
r = 0

while l < len(s1) and r < len(s2):
    if s1[l].lower() < s2[r].lower():
        print(-1)
        break
    elif s1[l].lower() > s2[r].lower():
        print(1)
        break
    else:
        l += 1
        r += 1
        
if l == len(s1) and r == len(s2):
    print(0)
    


