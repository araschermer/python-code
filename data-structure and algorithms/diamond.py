class ONE:
    def method(self):
        print("Method of class ONE ")


class TWO(ONE):
    def method(self):
        print("Method of class TWO ")


class THREE(ONE):
    def method(self):
        print("Method of class THREE ")


class FOUR1(TWO, THREE):
    pass


class FOUR2(THREE, TWO):
    pass


if __name__ == "__main__":
    four1 = FOUR1()
    # the order of the inheritance hierarchy in class FOUR1 is : class TWO before class THREE
    # Therefore it would print Method of class TWO
    four1.method()
    #
    # the order of the inheritance hierarchy in class FOUR2 is : class THREE before class TWO
    # Therefore it would print Method of class THREE
    four2 = FOUR2()
    four2.method()
