#oops - 1 year - 100 concepts
# (10 years - 25% oops concepts) - 25 concepts
#how many customers uses oops concept in data engineering space - everyone uses
#100 concepts - 5 concepts (i am going to cover now)
#is it mandatory to learn - yes, 5 concepts
#5 concepts we have to know to work as a DE/CE/CDE/AI Engg
#not needed (5 hours video interested) - databricks/spark/ai ...
#misc concepts: inherit,poly morp, overload,overriding, abstraction, encapsulation, constructors, inst met, class met, static met...
#1. Class - Class is template or a blueprint program that contains related members in a form of sub classes,functions, variables
class cls1:
    def __init__(self):
        self.abcd=100
    @staticmethod#decorator
    def fun1(self,x,y):return x+y+self.abcd
#2. Members - the functions/variable/sub classes created inside a class
#fun1 is the member of the cls1 because it uses first self param and
#self.x is member attribute/variable
#3. Object (obj1) - Instance of a Class (reference) - memory reference of a class
obj1=cls1()#refer the constructed class using a variable (object)
print(obj1.fun1(10,20))#finally access the members
print(obj1.fun1(20,20))#finally access the members
#4. Constructor ()- Construction of object from a class in memory using
cls1()#construct the class
#5. self argument - self parameter is the first parameter (automatically defined) when u create a member.
#self holds the class(object) reference
# Class in the hierarchy of python program oops+fbp - pkg/subpkg/module/CLASS/functions


#1. Class - Class is template or a blueprint program that contains related members in a
# form of sub classes,functions, variables
#2. Members - the functions/variable/sub classes created inside a class
class Class1_Connection_sources:#google sheet (Harddisk)
    def fun1(self,a,b):#tab1 (member1)
        return a+b
    def fun2(self,a,b,c):#tab2 (member2)
        return a+b+c
    var1=10
    class SubClass:
        print("hello")
class Class2_Connection_targets:#google sheet
    def fun1(self,x,y):#tab1 (member1)
        return x+y
    def fun2(self,x,y,z):#tab2 (member2)
        return x+y+z

obj1=Class1_Connection_sources()
print(obj1.fun1(10,20))

#3. Object - Instance of a Class (reference) - memory reference of a class
#4. Constructor ()- Construction of class to load in the memory
obj1=Class1_Connection_sources()#by applying () on the class name, i am instantiating/loading/initializing the class in memory
#Class1_Connection_sources is a? class (gsheet link kept in google)
#obj1 is a? object reference (chrome tab referring the url loaded in the memory)
# () is a ? constructor who load the class in memory (if we click the link, that loaded in the memory)
# obj1.fun1 is a? member (the tabs inside the sheet loaded in memory, i will use chrome browsertab.sheet-tab

#Understanding the concepts of members and self argument
#question: if we keep anything inside a class, will it be a member? no, we can control it
#question: can a variable be a member?
#question: can we pass argument to a class?
class IrfanFamilyCls:#initial (self argument)
    def son1(self,a,b):return a+b
    def daughter1(abcd, a, b): return a + b
    @staticmethod#not a member
    def driver(a):return a*a

obj1=IrfanFamilyCls()
print(obj1.son1(10,20))

#question: can a variable be a member? yes, it can, if we assign self.variablename
#question: can we pass argument to a class? yes we can
class IrfanFamilyCls2:#parameterized constructor class
    variable1=10
    def __init__(self,arg1):
        print("argument1 passed as a parameter, when constructing the class", arg1)
        self.memberattribute=arg1
    def son1(self,a,b):return a+b
    def daughter1(self, a, b): return a + b + self.memberattribute

obj1=IrfanFamilyCls2('argument to the class')
print(obj1.son1(10,20))
