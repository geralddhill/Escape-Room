from door import Door
import random
import check_input
class BasicDoor(Door):
    '''BasicDoor class represents a basic door
            Attributes:
                _solution: int
                _input: int
    '''
    def __init__(self):
        '''constructor'''
        self._solution = random.randint(1,2)
        self._input = 0
    def examine_door(self):
        '''returns a string description of the door.'''
        return f"You encounter a basic door, you can either push it or pull it to open."
    def menu_options(self):
        '''returns a string with the menu options that user can choose from
           when attempting to unlock the door.'''
        return f"1. Push\n2. Pull"
    def get_menu_max(self):
        '''returns the number of options in the above menu for check input.'''
        return 2
    def attempt(self, option):
        '''passes in the user’s menu selection. Use this value to update the
           input attribute. Return a string describing the user’s attempt'''
        self._input = option
        if self._input == 1:
            return f"You push the door"
        else:
            return f"You pull the door"
    def is_unlocked(self):
        '''checks to see if the door was unlocked by comparing the input
           attribute with the solution. Returns true if it is unlocked, false otherwise'''
        if self._input == self._solution:
            return True
        else:
            return False
    def clue(self):
        '''returns a hint for the user if their attempt was unsuccessful'''
        return f"Try another way"
    def success(self):
        '''returns a congratulatory message if the user attempt was successful.'''
        return f"Congratulations, you opened the door."
        
b = BasicDoor()
print(b.menu_options())
print(b.attempt(1))
print(b.is_unlocked())
