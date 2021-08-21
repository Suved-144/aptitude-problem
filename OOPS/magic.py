class emp():
    increment = 1.5

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.increment = 3

    def increses(self):
        self.salary = int(self.salary * self.increment)
    def __add__(self, other):
        return self.salary + other.salary
    def __repr__(self):
        return "Employee Name :  {} {} experiance {}  ".format(self.fname,self.lname,self.salary)
    def __str__(self):
        return "The name of emp is {} {} ".format(self.fname, self.lname)
    @staticmethod
    def isopen(day):
        if day == "sunday":
            return False
        else:
            return True
mahesh = emp("mahesh ", "gaikwad" , 5)
kunal = emp("kunal", "gunjal", 6)
suran =emp("kunal", "gunjal", 6)

print(str(mahesh))
print(repr(kunal))
#mahesh = programmer("Mahesh", "Gaikwad", 5, "java", 8)
# print(mahesh.fname)
# print(mahesh.lname)
#print("befor Salary  : ", mahesh.salary)
#mahesh.increses()
#print("after  Salary : ",mahesh.salary)
#print("experiance  : ",mahesh.exp)
#kunal = emp("kunal", "gunjal", 6)

#print("Kunal Salary  :  " , kunal.salary)
#kunal.increses()
#print("after Kunal Salary  :  " , kunal.salary)
