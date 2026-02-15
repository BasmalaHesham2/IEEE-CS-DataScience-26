n=int(input())
records=[]
grades=[]

if n>=2 and n<=5:
    for i in range(n):
        name=input()
        grade=float(input())
        grades.append(grade)
        records.append([name,grade])
    unique_grades=sorted(set(grades))
    s_grade=unique_grades[1]
    s_student=[]
    
    for x in records:
        if x[1]==s_grade:
            s_student.append(x[0])
    s_student.sort()
    for s in s_student:
        print(s)
