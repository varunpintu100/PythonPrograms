class Employee:#class employee initializes the class attributes
    def __init__(self,name,ref,age,gender):
        self.name=name
        self.ref=ref
        self.age=age
        self.gender=gender
class Organisation:
    def __init__(self,org_name,emp):
        self.org_name=org_name
        self.emp=emp
    def addEmployee(self,name,ref,age,gender):
        self.emp.append(Employee(name,ref,age,gender))
    def getEmployeeCount(self):
        return len(self.emp)
    def findEmployeeAge(self,ref):
        for i in self.emp:
            if i.ref==ref:
                return i.age
        return -1
    def countEmployees(self,age):
        count =0
        for i in self.emp:
            if i.age > age :
                count +=1
        return count

if __name__ == '__main__':
    employees=[]
    o = Organisation('XYZ',employees)
    n=int(input())
    for i in range(n):
        name=input()
        id1=int(input())
        age=int(input())
        gender=input()
        o.addEmployee(name,id1,age,gender)
    id1=int(input())
    age=int(input())
    print(o.getEmployeeCount())
    print(o.findEmployeeAge(id1))
    print(o.countEmployees(age))