#Charles Ajjan
#CMP131
#Week 08
#Lab 01
#Loop Patterns
#Date started 10-21-2026
print("Loop Pattern Generator: Increasing and Decreasing Patterns")
print()

print("Pattern A: Increasing Pattern")
for i in range(10):
    row = ""
    for count in range(i + 1):
        row = row + "+"
    print(row)

print()
print("Pattern B: Decreasing Pattern")
for i in range(10):
    row = ""
    for count in range(10 - i):
        row = row + "+"
    print(row)
