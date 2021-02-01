import random as rand
import string

class Robot:
    def __init__(self):
        self.name = self.generateRandomName()

    def generateRandomName(self):
        alphabet = string.ascii_uppercase
        num_list = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
        random_letter1 = rand.choice(alphabet)
        random_letter2 = rand.choice(alphabet)
        random_num1 = rand.choice(num_list)
        random_num2 = rand.choice(num_list)
        random_num3 = rand.choice(num_list)
        return f"{random_letter1}{random_letter2}{random_num1}{random_num2}{random_num3}"

    def reset(self):
        new_name = self.generateRandomName()
        if self.name == new_name:
            new_name = self.generateRandomName()
        self.name = new_name