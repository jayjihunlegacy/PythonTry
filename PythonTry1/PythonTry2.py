'''
# 1. __init__
class Person:
    def sayhi(self):
        print("HELLO",self.name);
    def __init__(self,name):
        print("ADVANCED");
        self.name=name;
p=Person("jay")
p.sayhi();
print(p.name);
'''
'''
# 2. basic class
class Robot:
    population=0;

    def __init__(self,name):
        self.name=name;
        print("INITIALIZING",self.name);
        Robot.population+=1

    def die(self):
        print(self.name,"is destroyed");
        Robot.population-=1
        if Robot.population==0:
            print(self.name,"was the last one");
        else:
            print("There are stil {} robots working.".format(Robot.population));
    def sayhi(self):
        print("Hello");

    @classmethod
    def howmany(cls):
        print("We have {} robots.".format(cls.population));
droid1 = Robot("R2-D2");
droid1.sayhi();
Robot.howmany();

droid2 = Robot("R3-D3");
droid2.sayhi();
Robot.howmany();

droid1.die();
droid2.die();

Robot.howmany();
'''
'''
# 3. inheritance
class SchoolMember:
    def __init__(self,name,age):
        self.name=name;
        self.age=age;
        print("INIT");
    
    def tell(self):
        print("Name : {}, Age : {}".format(self.name,self.age));

class Teacher(SchoolMember):
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary=salary;
        print("INIT TEACHER");

    def tell(self):
        SchoolMember.tell(self);
        print("Salary :",self.salary);

class Student(SchoolMember):
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age);
        self.marks=marks;
        print("INIT STUDENT");

    def tell(self):
        SchoolMember.tell(self);
        print("Marks :",self.marks);

t = Teacher("soohwan",40,30000)
s = Student("Jay",25,75);
print("");
members=[t,s];
for member in members:
    member.tell();
'''

def is_palindrome(text):
    return text==text[::-1];

input = input("Enter text : ");
if is_palindrome(input):
    print("YES");
else:
    print("NO");