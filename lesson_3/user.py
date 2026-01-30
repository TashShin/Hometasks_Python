class User:

    def __init__(self, first_name, second_name):
        self.first_name = first_name
        self.second_name = second_name

    def get_first_name(self):
        print(self.first_name)

    def get_second_name(self):
        print(self.second_name)

    def get_full_name(self):
        print(f"{self.first_name} {self.second_name}")
