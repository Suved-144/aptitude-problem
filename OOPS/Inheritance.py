class emp():
    increment = 1.5
    def __init__(self,fname, lname , salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.increment = 3

    def increses(self):
        self.salary= int(self.salary*self.increment)
mahesh = emp("Mahesh","Gaikwad",5)
#print(mahesh.fname)
#print(mahesh.lname)
print(mahesh.salary)
mahesh.increses()
print(mahesh.salary)
kunal = emp("kunal", "gunjal", 6)

class programmer(emp):
    def __init__(self,fname,lname,salary,progl, exp):
        super().__init__(fname,lname,salary)
        self.progl = progl
        self.exp = exp
    def increses(self):
        self.salary= int(self.salary * (self.increment + 1 ))
        

digvijay = programmer("digvijay", "raj",9 ,"python", "5 yrs")
print(digvijay.fname)
print(digvijay.exp)
digvijay.increses()
print(digvijay.salary)
print(digvijay.increses())
#print(digvijay.fname)
#print(digvijay.lname)
#print(digvijay.salary)
