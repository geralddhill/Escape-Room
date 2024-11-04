from door_factory import DoorFactory
import random
from combo_door import ComboDoor
from deadbolt_door import DeadboltDoor
from code_door import CodeDoor
class DifficultDoorFactory(DoorFactory):
    """Door factory that creates an instance or a random difficult door.
    """

    def create_door(self):
        """Factory method to create an instance of a door.

        Chooses randomly between ComboDoor, DeadboltDoor, and CodeDoor.

        :return: Door instance
        """
        door_choice = random.randint(1,3)
        
        if door_choice == 1:
            # return ComboDoor
            return ComboDoor()
        elif door_choice == 2:
            # return DeadboltDoor
            return DeadboltDoor()
        else:
            # return CodeDoor
            return CodeDoor()