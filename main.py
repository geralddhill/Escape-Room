# Names: Gerald Hill, Hoang Do
# Date: 11/4/24
# Desc: Simulates a user having to open three kinds of doors. Uses factory pattern to implement.

from door import Door
from check_input import get_int_range

def open_door(door: Door) -> None:
    """

    :param door: Door object that the user will try to unlock
    """
    print(door.examine_door())
    unlocked = False

    while not unlocked:
        print(door.menu_options())
        user_input: int = get_int_range("Enter choice: ", 1, door.get_menu_max())
        print(door.attempt(user_input))

        unlocked = door.is_unlocked()
        if unlocked:
            print(door.success())
        else:
            print(door.clue())



def main() -> None:
    """Simulates a user having to open three kinds of doors.

    Uses factory pattern to implement.
    """