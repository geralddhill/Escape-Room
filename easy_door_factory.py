from door import Door

class EasyDoorFactory(Door):
    """Door factory that creates an instance or a random easy door.
    """

    def create_door(self) -> Door:
        """Factory method to create an instance of a door.

        Chooses randomly between BasicDoor, LockedDoor, and ComboDoor.

        :return: Door instance
        """
