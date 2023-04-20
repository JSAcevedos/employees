m = int(input())
skills = input().split()
n = int(input())
potential_employees = 0

for i in range(n):
    candidate = input().split()
    fulfill = 0
    if len(candidate) >= m:
        for j in skills:
            if j in candidate:
                fulfill += 1
            else:
                break
    else:
        continue
    if fulfill == len(skills):
        potential_employees += 1

print(potential_employees, end="")