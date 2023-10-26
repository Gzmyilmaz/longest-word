
import string
import random
import requests

class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))
        pass

    def is_valid(self, word: str) -> bool:

        if not word:
            return False
        letters = self.grid.copy() # Consume letters from the grid
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        return self.__check_dictionary(word)
    @staticmethod
    def __check_dictionary(word):
        response = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}")
        json_response = response.json()
        return json_response['found']
game = Game()
#print("hello")
print(game.grid) # --> OQUWRBAZE
my_word = "BAROQUE"
game.is_valid(my_word) # --> True
