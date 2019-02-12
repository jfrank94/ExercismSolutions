import random
import string








class Robot(object):
    robot_name_space = set()

    def __init__(self):
        self.name = self.generate_random_name_choice()

    def generate_name(self):
        random_letter = [random.choice(string.ascii_letters.upper())for i in range(2)]
        random_num = [str(random.randrange(10)) for i in range(3)]
        robot_name = random_letter + random_num
        return ''.join(robot_name)

    def generate_random_name_choice(self):
        name = self.generate_name()
        while name in self.robot_name_space:
            name = self.generate_name()
        self.robot_name_space.add(name)
        return name

    def reset(self):
        return self.__init__()
