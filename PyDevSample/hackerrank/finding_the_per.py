if __name__=='__main__':
    n=int(input())
    sum1=0
    student_marks={}
    for i in range(n):
        name,*line=input().split()
        scores=list(map(float,line))
        student_marks[name]=scores
    query_name=input()
    for marks in student_marks[query_name]:
        sum1=marks+sum1
    print(sum1/3)