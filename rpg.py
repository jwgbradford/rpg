INSTRUCTIONS = '''Role Playing Game

Commands
========
go [direction] : move in direction'''

class MyGame:
    def __init__(self):
        self.main_loop()

    def show_instructions(self):
        print(INSTRUCTIONS)

    def main_loop(self):
        while True:
            self.show_instructions()
            command = input('\n>')

if __name__ == "__main__":
    rpg = MyGame()

