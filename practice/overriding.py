class a:
    def method1(self):
        print("IN Class A")


class b(a):
    def method1(self):
        print("IN Class B")


class c(a):
    def method1(self):
        print("IN Class C")


class d(a):
    def method1(self):
        super().method1()
        print("IN Class D")
a= a()
b= b()
c= c()
d= d()
a.method1()
b.method1()
c.method1()
d.method1()
