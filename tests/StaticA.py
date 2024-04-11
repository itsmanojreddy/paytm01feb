class staticA:
    @staticmethod
    def m1():
        print("method 1 in non static")

    def m2(self):
        print("method 2 in non static")
        self.m1()
    if __name__ == "__main__":
        m1()
