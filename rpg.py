import json

INSTRUCTIONS = '''Role Playing Game

Commands
========
go [direction] : move in direction'''

class MyGame:
    def __init__(self):
        self.rooms = self.build_world()
        self.current_room = 0
        self.main_loop()

    def build_world(self):
        file_name = 'world_data.txt'
        with open(file_name) as file:
            world_data = json.load(file)
        file.closed
        list_of_rooms = []
        for data in world_data.items():
            room_UID = data[0]
            room_data = data[1]
            room_name = room_data[0]
            room_description = room_data[1]
            room_contents = room_data[2]
            room_doors = room_contents["doors"]
            list_of_doors = []
            for door in room_doors:
                door_name = door[0]
                door_description = door[1]
                door_direction = door[2]
                door_leads_to_UID = door[3]
                door_instance = Door(door_name, door_description, door_direction, door_leads_to_UID)
                list_of_doors.append(door_instance)
            room_instance = Room(room_UID, room_name, room_description, list_of_doors)
            list_of_rooms.append(room_instance)
        return list_of_rooms

    def show_instructions(self):
        print(INSTRUCTIONS)

    def main_loop(self):
        while True:
            self.show_instructions()
            print(self.rooms[self.current_room].description)
            command = input('\n>')

class GameObject:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Room(GameObject):
    def __init__(self, UID, name, description, doors):
        super().__init__(name, description)
        self.UID = UID
        self.doors = doors

class Door(GameObject):
    def __init__(self, name, description, direction, room_UID):
        super().__init__(name, description)
        self.direction = direction
        self.linked_room = room_UID

if __name__ == "__main__":
    rpg = MyGame()

