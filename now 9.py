import time
import sys
class Add:
    def __init__(self):
        self.n1=1
        self.n2=2
        self.n3=3
        self.n4=4
        self.n5=5
        self.n6=6
        self.sum=0

    def display(self):
        print("number:",self.n1,self.n2,self.n3,self.n4,self.n5,self.n6)
        print("Sum:", self.sum)
    def find_sum(self):
        self.sum=self.n1+self.n2+self.n3+self.n4+self.n5+self.n6
s=time.time()
c1=Add()
c1.find_sum()
c1.display()
e=time.time()
print("time required(without array)=",e-s)
space=sys.getsizeof(c1)
print("space utalization in bytes=",space)
        
