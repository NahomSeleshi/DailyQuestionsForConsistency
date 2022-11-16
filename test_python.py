class PrintName:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    def print_only(self):
        print("The name in the constructor is: ", self.name, " and the age is: ", self.age)
    def print_name(self, name):
        print("The given name is: ", name)
p_name = PrintName("Nahom1", 25)
p_name.print_only()
p_name.print_name("Nahom")