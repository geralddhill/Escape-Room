from door import Door

class DiffucultDoorFactory(Door):
    """Door factory that creates an instance or a random diffucult door.
    """

    def create_door(self) -> Door:
        """Factory method to create an instance of a door.

        Chooses randomly between ComboDoor, DeadboltDoor, and CodeDoor.

        :return: Door instance
        """
        