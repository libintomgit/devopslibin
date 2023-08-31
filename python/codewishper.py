

#function to add 2 numbers

class  Calculator:
    def __init__(self):
        self.a=0
        self.b=0
        self.result=0

    def add(self,a,b):
        self.a=a
        self.b=b
        self.result=self.a+self.b
        return self.result

    def sub(self,a,b):
        self.a=a
        self.b=b
        self.result=self.a-self.b
        return self.result

    def mul(self,a,b):
        self.a=a
        self.b=b
        self.result=self.a*self.b
        return self.result

    def div(self,a,b):
        self.a=a
        self.b=b
        self.result=self.a/self.b
        return self.result


obj=Calculator()
print(obj.add(10,20))

print(obj.sub(20,10))
print(obj.mul(20,10))
print(obj.div(20,10))
print(obj.result)


