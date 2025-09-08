class Programmer:
    company="Microsoft"
    def __init__(self,name,salary,position):
        self.name=name
        self.salary=salary
        self.position=position
p=Programmer("Priyanshu",1300000,"Developer")
print(p.name,p.salary,p.position,p.company)
q=Programmer("Rita",1400000,"Project Manager")
print(q.name,q.position,q.salary,q.company)
        
