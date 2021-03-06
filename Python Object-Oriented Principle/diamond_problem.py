class BaseClass:
    no_of_BaseCalls = 0

    def call_me(self):
        print("Calling base class")
        BaseClass.no_of_BaseCalls += 1


class LeftSubclass(BaseClass):
    no_of_leftCalls = 0

    def call_me(self):
        BaseClass.call_me(self)
        print("Callling left subclass")
        LeftSubclass.no_of_leftCalls += 1


class RightSubclass(BaseClass):
    no_of_rightCalls = 0

    def call_me(self):
        BaseClass.call_me(self)
        print("Calling right subclass")
        RightSubclass.no_of_rightCalls += 1


class Subclass(LeftSubclass, RightSubclass):
    no_of_subCalls = 0

    def call_me(self):
        LeftSubclass.call_me(self)
        RightSubclass.call_me(self)
        print("Calling subclass")
        self.no_of_subCalls += 1
