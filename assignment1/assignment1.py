# -----------------------------Question 1---------------------------------------------------------------

n = int(input("Enter no of students\n"))

if (1 < n < 6):
    students = []
    # students = [['Berry', '37.21'], ['akriti', '41'], [
    #     'harr', '37.21'], ['harsh39', '39'], ['tina', '37.2']]
    for i in range(n):
        students.append([input(), input()])

    sorted_scores = sorted(list(set([x[1] for x in students])))
    second_lowest = sorted_scores[1]
    low_final_list = []
    for student in students:
        if second_lowest == student[1]:
            low_final_list.append(student[0])
    for student in sorted(low_final_list):
        print(student)
else:
    print("wrong constraint")


# -----------------------------Question 2---------------------------------------------------------------
s = input("Enter a string\n")
vowels = 'AEIOUaeiou'
kev = 0
stu = 0
for i in range(len(s)):
    if s[i] in vowels:
        kev += (len(s)-i)
    else:
        stu += (len(s)-i)

if kev > stu:
    print("Kevin", kev)
elif kev < stu:
    print("Stuart", stu)
else:
    print("Draw")

# -----------------------------Question 3---------------------------------------------------------------
n = int(input("Enter the size of array\n"))
if 1 < n < 11:
    arr = map(int, input().split())
    arr = list(set(list(arr)))
    arrayLen = len(arr)
    arr = sorted(arr)
    print(arr[arrayLen-2])
else:
    print("n size must be between 2 and 10")
