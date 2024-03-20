class overloading:
    def method(self):
        print("first method")

    def method(self, p1):
        print("Second method")
        print(p1)

    def method(self, p1, p2):
        print("third method")
        print(p1)
        print(p2)

    def method(self, *args):
        print("Args method")
        for i in args:
            print(i)


o = overloading()
o.method(1)
