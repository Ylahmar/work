class MyTime:
    def __init__(self,hrs=0,mins=0,secs=0):
        totalsecs = hrs*3600 + mins*60 + secs
        if totalsecs < 0:
            print("Not Possiable Time Can not be negative, totalsecs will equal to 0!")
            totalsecs = 0
        self.hours = totalsecs // 3600        
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60
    def between(self, t1, t2):
        if t1 <= self and self < t2:
            print("True")
        else:
            print("False")
        def __str__(self):
            return "({0},{1},{2})".format(self.hours, self.minutes, self.seconds)

       
       def to_seconds(self):
           return self.hours * 3600 + self.minutes * 60 + self.seconds

       def __eq__(self, other):
           return self.to_seconds() == other.to_seconds()

       def __le__(self, other):
           return self.to_seconds() <= other.to_seconds()

       def __ge__(self, other):
           return self.to_seconds() >= other.to_seconds()

       def __gt__(self, other):
           return self.to_seconds() > other.to_seconds()

       def __lt__(self, other):
           return self.to_seconds() < other.to_seconds()

       def __ne__(self, other):
           return self.to_seconds() != other.to_seconds()

       def increment(self, seconds):
           total_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds
           if total_seconds + seconds >= 0:
               total_seconds += seconds
               self.hours = int(total_seconds/3600)
               self.minutes = int((total_seconds%3600)/60)
               self.seconds = int((total_seconds%3600)%60)
           else:
               print("Negative increment of seconds cannot exceed total time.")

       def increment_test(self, seconds):
           self.seconds += seconds

           while self.seconds >= 60:
               self.seconds -= 60
               self.minutes += 1

           while self.minutes >= 60:
               self.minutes -= 60
               self.hours += 1
             
       def between(t1, t2, obj):
           if t1 <= t2:
               if t1 <= obj and obj < t2:
                   return True
               else:
                   return False

    def add_time(t1, t2):
       secs = t1.to_seconds() + t2.to_seconds()
       return MyTime(0, 0, secs)

t1 = MyTime(3,170,340)
t1_test = MyTime(3,170,340)
t2 = MyTime(5,60,1)
t2_test = MyTime(5,60,1)
t3 = MyTime(3,50,34)
t3_test = MyTime(3,50,34)
t4 = MyTime(2,70,140)
t4_test = MyTime(2,70,140)

print("The lines below tests out the between method from MyTime class.")
print("\nBelow should print out False given code: MyTime.between(t1, t2, MyTime(0,0,0))")
print(MyTime.between(t1, t2, MyTime(0,0,0)))
print("Below should print out True given code: MyTime.between(t4, t3, MyTime(3,15,5))")
print(MyTime.between(t4, t3, MyTime(3,15,5)))
print("\n\nThe lines below tests out the enhanced increment method and compares it")
print("with the increment method given")
print("\nTest 1:")
t1.increment(60)
print(t1)
t1_test.increment_test(60)
print(t1_test)

print("\nTest 2:")
t2.increment(540)
print(t2)
t2_test.increment_test(540)
print(t2_test)

print("\nTest 3:")
t3.increment(174)
print(t3)
t3_test.increment_test(174)
print(t3_test)

print("\nTest 4 shows why computers cannot subtract more time than there is.\nTest 4:")
t4.increment(-11541)
print(t4)
t4_test.increment_test(-11541)
print(t4_test)
