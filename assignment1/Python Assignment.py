#Question 1

N=int(input())
students=[]
secondminarray=[]
flag=0
for i in range(0,N):
    name=input()
    mark=float(input())
    students.append([name,mark])
students.sort(key=lambda x:x[1])
for i in range (0,N-1):
    if flag==0:
        if(students[i][1]!=students[i+1][1]):
            secondminvalue=students[i+1][1]
            secondminarray.append(students[i+1][0])
            flag=1
            continue
    if flag==1:
        if(secondminvalue==students[i+1][1]):
            secondminarray.append(students[i+1][0])
secondminarray.sort()
result="\n".join(secondminarray)
print(result)

#Question 2

S=(input()).lower()
x=('a','e','i','o','u')
Stuart,Kevin=0,0
for i in range(0,len(S)):
    for j in range(1+i,len(S)+1):
        if(S[i:j].startswith(x)):
            Kevin+=1
        else:
            Stuart+=1
if Kevin>Stuart:
    print("Kevin",Kevin)
elif Stuart>Kevin:
    print("Stuart",Stuart)
else:
    print("Draw")


#Question 3

n=int(input())
score_sheet=list(map(int,input().split()))
second_max_score=-101,-101
max_score=0
for i in range(0,n):
    if(score_sheet[i]>max_score):
        second_max_score=max_score
        max_score=score_sheet[i]
    elif(score_sheet[i]>second_max_score and score_sheet[i]!=max_score):
        second_max_score=score_sheet[i]
print(second_max_score)
