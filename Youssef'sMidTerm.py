#Youssef Lahmar 
class RutgersStudent:
    def __init__(self,lastname,i_d):
        self.i_d = i_d
        self.lastname = lastname
        self.creditsEarned = 0
        self.status = 0
        self.courseLoadCredits = 0
    
       
    def registerCourse(self,credit):
        # Youssef : I put  2 if statements the first one is to
        #to make the credit that is under 0 will give u a erro message
        #because it cant be 0. The Other If statement I imputed was if its greater
        #than 18 it will give another erro because it cant be greater than 18
        if(credit<0):
           return "Credit must be positive it cant be negatavie!!!!!! "
           return
        if credit <= 18:
            
            self.courseLoadCredits += credit
            
            return "Registered in the course CONGRATS"
        else:
            return "Erro The Total credit load cant pass 18 TRY AGAIN"
    def withdraw(self,credit):
       if self.courseLoadCredits - credit < 0:
           print("IT is not  possible to remove the course at the moment")
           return
       else:
           self.courseLoadCredits -= credit
           return "You are Withdrawn from the course"
    


    def createEmail(self):
        self.email = self.lastname + str(self.i_d) + '@rutgers.edu'
        return self.email
        
    def passedCourse(self,credit):
       self.courseLoadCredits -= credit
       self.creditsEarned += credit
       # 5 is the gradute becuase you said no matter how much credits he earned
       #he still graduated.
       
       if self.status == 5:
           pass
       # over here you just add if you eqaul or under 30 your a freshman
       #and it keeps going to senior
       elif self.creditsEarned >= 90 and self.creditsEarned < 120:
           self.status = 4
       elif self.creditsEarned >= 60 and self.creditsEarned < 90:
           self.status = 3
       elif self.creditsEarned >= 30 and self.creditsEarned < 60:
           self.status = 2
       elif self.creditsEarned <= 30:
           self.status = 1
       return "!!!! Course Passed !!!!!!"

    def get_lastname(self):
        return self.lastname
    def get_i_d(self):
        return self.i_d
    def get_satus(self):
        return self.satus

class Graduate_Student(RutgersStudent):
    def __init__(self,lastname,i_d):
       RutgersStudent.__init__(self,lastname,i_d)
       #I MADE IT SELF.STATUS 5 BECUASE FOR NO MATTER WHAT THE INT IS IT WILL
       #ALWAYS BE SELF.STATUS 5
       self.status = 5
    def registerCourse(self,credit): 
        if(credit<0):
           return "!!!!Credit must be positive it cant be negatavie!!!!!! "

        if credit <= 15:
            
            self.courseLoadCredits += credit
            
            return "Registered in the course CONGRATS"
        else:
            return "Erro The Total credit load cant pass 15 Erro"
            

        

student = RutgersStudent('Lahmar',292)
GraduateStudent = Graduate_Student('Riley',108)
print('Last Name =', student.get_lastname())
print('Student ID  =', student.get_i_d())
print('Student Email  =', student.createEmail())
print('registerCourse  =', student.registerCourse(5))
print('registerCourse  =', student.registerCourse(3))
print('registerCourse  =', student.registerCourse(2))
print('registerCourse  =', student.registerCourse(10))
print('registerCourse  =', student.registerCourse(15))
print('registerCourse  =', student.registerCourse(15))
print('registerCourse  =', student.registerCourse(19))
print('registerCourse  =', student.registerCourse(-10))
print('Passed The course  =', student.passedCourse(4))
print('Passed The course  =', student.passedCourse(4))
print('Passed The course  =', student.passedCourse(3))
print('Passed The course  =', student.passedCourse(10))
print('Passed The course  =', student.passedCourse(15))
print('Passed The course  =', student.passedCourse(12))
print('withdraw  =', student.withdraw(1))
print("The status of the student is",student.status)
#GraduateStudent
print("------------------------------------------------------------")
print("GraduateStudent")
print('Last Name =', GraduateStudent.get_lastname())
print('Student ID  =', GraduateStudent.get_i_d())
print('Student Email  =', GraduateStudent.createEmail())
print('registerCourse  =', GraduateStudent.registerCourse(5))
print('registerCourse  =', GraduateStudent.registerCourse(3))
print('registerCourse  =', GraduateStudent.registerCourse(2))
print('registerCourse  =', GraduateStudent.registerCourse(10))
print('registerCourse  =', GraduateStudent.registerCourse(15))
print('registerCourse  =', GraduateStudent.registerCourse(15))
print('registerCourse  =', GraduateStudent.registerCourse(19))
print('registerCourse  =', GraduateStudent.registerCourse(-10))
print('Passed The course  =', GraduateStudent.passedCourse(4))
print('Passed The course  =', GraduateStudent.passedCourse(4))
print('Passed The course  =', GraduateStudent.passedCourse(3))
print('Passed The course  =', GraduateStudent.passedCourse(10))
print('Passed The course  =', GraduateStudent.passedCourse(15))
print('Passed The course  =', GraduateStudent.passedCourse(12))
print('withdraw  =', GraduateStudent.withdraw(1))
print("The status of the student is",GraduateStudent.status)
GraduateStudent = int(input("CONGRATS YOU GRADUATED, You finshed press(0 to quit): "))

    

