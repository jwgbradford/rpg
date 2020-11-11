import json

INSTRUCTIONS = '''Role Playing Game
Commands
========
go [direction] : move in direction'''

class MyGame:
    def __init__(self):
        self.rooms = self.build_world()
        self.current_room = "0"
        self.main_loop()

    def build_world(self):
        file_name = 'world_data_2.txt'
        with open(file_name) as file:
            world_data = json.load(file)
        file.closed
        dict_of_rooms = {}
        for room_data in world_data:
            room_UID = room_data["UID"]
            room_name = room_data["name"]
            room_description = room_data["description"]
            room_contents = room_data["contents"]
            room_doors = room_contents["doors"]
            list_of_doors = []
            for door in room_doors:
                door_name = door["name"]
                door_description = door["description"]
                door_direction = door["direction"]
                door_leads_to_UID = door["connects_to"]
                door_instance = Door(door_name, 
                                    door_description, 
                                    door_direction, 
                                    door_leads_to_UID)
                list_of_doors.append(door_instance)
            room_instance = Room(room_UID,
                                room_name, 
                                room_description, 
                                list_of_doors
                                )
            dict_of_rooms[room_UID] = room_instance
        return dict_of_rooms

    def show_instructions(self):
        print(INSTRUCTIONS)

    def main_loop(self):
        while True:
            self.show_instructions()
            print('You are in', self.rooms[self.current_room].name.lower() +'.')
            command = input('\n>')
            self.parse(command)

    def parse(self, cmd):
        cmd = cmd.lower().split()
        if len(cmd) == 0:
            print('You forgot to type anything')
        elif len(cmd) == 2:
            action, modifier = cmd
            if action == 'go':
                direction = modifier
                self.current_room = self.rooms[self.current_room].move(direction)
            else:
                print('I don\'t know how to do that.')
        else:
            print('I\'m not sure what you mean.')
        return

class GameObject:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Room(GameObject):
    def __init__(self, room_UID, name, description, doors):
        super().__init__(name, description)
        self.UID = room_UID
        self.doors = doors

    def move(self, direction):
        for door in self.doors:
            if door.direction.lower() == direction:
                print('You move', door.direction + '.')
                return door.linked_room
        print('You cannot go', direction)
        return self.UID

class Door(GameObject):
    def __init__(self, name, description, direction, room_UID):
        super().__init__(name, description)
        self.direction = direction
        self.linked_room = room_UID

if __name__ == "__main__":
    rpg = MyGame()
