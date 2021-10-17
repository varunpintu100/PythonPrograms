class Employee:
    raise_amount=1.04
    def __init__(self,name,pay):
        self.name=name
        self.mail=name+'@gmail.com'
        self.pay=pay
    def applyraise(self):
        return self.pay*self.raise_amount
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount=amount
class Developer(Employee):
    raise_amount=1.10
    def __init__(self,name,pay,prog_lang):
        super().__init__(name,pay)
        self.prog_lang=prog_lang
class Manager(Employee):
    def __init__(self,name,pay,emp_num=None):
        super().__init__(name,pay)
        if emp_num is None:
            self.emp_num=[]
        else:
            self.emp_num = emp_num
    def add_emp(self,emp):
        if emp not in self.emp_num:
            self.emp_num.append(emp)
    def rem_emp(self,emp):
        if emp  in self.emp_num:
            self.emp_num.remove(emp)
    def print_emp(self):
        for emp in self.emp_num:
            print("-----> {} ".format(emp.name))
if __name__=='__main__':
    st=input()
    name,salary,lang=st.split(" ")
    dev2=Developer(name,salary,lang)
    print(dev2.__dict__)
    dev1=Developer('varun',10000,'python')
    dev2=Developer('vamshi',10000,'Java')
    mgr1=Manager('sonu',1000,[dev1])
    emp1=Employee('vedhanth',5000)
    print(isinstance(mgr1,Manager))
    print(issubclass(Manager,Employee))