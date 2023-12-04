#D. King Escape

n = int(input())
ax, ay = map(int, input().split()) # Queen's position
bx, by = map(int, input().split()) # King's position
cx, cy = map(int, input().split()) #Goal

"""
Queen can't attacked Goal.
Bob ini poistion can't be attacked.
Three distinct coordinates.

We can bypass diagonals but not horizontals and verticals.
"""

if 1 <= cx <= ax and 1 <= cy <= ay:
    print("YES")
else:
    print("NO")




    
    