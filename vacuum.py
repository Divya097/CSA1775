class VacuumCleaner:
    def __init__(self, room_size):
        self.room_size = room_size
        self.room = [['.' for _ in range(room_size)] for _ in range(room_size)]
        self.x, self.y = 0, 0  # Initial position of the vacuum cleaner
        self.cleaned = 0

    def move_up(self):
        if self.x > 0:
            self.x -= 1
            print(f"Moved up to ({self.x}, {self.y})")

    def move_down(self):
        if self.x < self.room_size - 1:
            self.x += 1
            print(f"Moved down to ({self.x}, {self.y})")

    def move_left(self):
        if self.y > 0:
            self.y -= 1
            print(f"Moved left to ({self.x}, {self.y})")

    def move_right(self):
        if self.y < self.room_size - 1:
            self.y += 1
            print(f"Moved right to ({self.x}, {self.y})")

    def clean(self):
        if self.room[self.x][self.y] == '.':
            self.room[self.x][self.y] = 'C'  # Mark the spot as cleaned
            self.cleaned += 1
            print(f"Cleaned position ({self.x}, {self.y})")

    def get_cleaned_count(self):
        return self.cleaned

    def show_room(self):
        for row in self.room:
            print(' '.join(row))

# Usage
vacuum = VacuumCleaner(5)
vacuum.show_room()

vacuum.move_right()
vacuum.move_down()
vacuum.clean()

vacuum.move_left()
vacuum.move_up()
vacuum.clean()

vacuum.show_room()
print(f"Total spots cleaned: {vacuum.get_cleaned_count()}")
