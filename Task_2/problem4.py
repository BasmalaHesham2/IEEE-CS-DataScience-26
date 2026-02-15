if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()

    for x in student_marks:
        suum=0
        lenn=0
        if(query_name==x):
            for y in student_marks[query_name]:
                suum+=y
                lenn=len(student_marks[query_name])
            print(f'{(suum/lenn):.2f}')
            
