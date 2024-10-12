class myfirstclass:
    name="arif"
    age=20
    instution=""

information=myfirstclass()
print(information.name)
information.instution="sonargo university"
print(information.instution)
#constrctor
class mysecondClass:
    def __init__(self,name, age) -> None:
        self.name=name
        self.age=age
        pass
     
    def __str__(self) -> str:
        return f"{self.name}({self.age})"
       
       
myinf=mysecondClass("sagor islam", 20)
print(myinf)

#inheritence
class course:
    def __init__(self,course, name, time) -> None:
        self.course=course
        self.name=name
        self.time=time
        pass

class student1(course):
    def __init__(self, course, name, time, studentname, age) -> None:
        super().__init__(course, name, time)
        self.studentname=studentname
        self.age=age
student_informtion=student1('HUM','dld','2hour','Mumin',30)
print(student_informtion.course)
print(student_informtion.studentname)

    




