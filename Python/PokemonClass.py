class Pokemon():

    def __init__ (self, pokemon_name, pokemon_type, pokedex_ID):
        """
        Attributes:
        1. We take in the 3 arguments above
        2. Assign them to self.name, self.type, and self.ID
        3. These 3 will be the attributes of my Pokemon Class
        """
        # Expect "name" to be a string
        self.name = pokemon_name

        # Expect "type" to be a string
        self.type = pokemon_type

        # Expect "ID" to be an integer
        self.ID = pokedex_ID

    def set_name(self, pokemon_name):
        """
        Creating the set_name method, which is a setter to UPDATE the name attribute!
        """
        if type(pokemon_name) == str:
            self.name = pokemon_name
            return True
        else:
            return False

    def get_name(self):
        """
        Creating the get_name method, which is a getter to retrieve the name attribute!
        """
        return self.name

    def set_ID(self, pokedex_ID):
        """
        Creating the set_ID method, which is another setter to UPDATE the ID attribute!
        """
        if type(pokedex_ID) != int:
            return False

        if pokedex_ID >= 1 and pokedex_ID <= 151:
            self.ID = pokedex_ID
            return True

    def get_ID(self):
        """
        Creating the get_ID method, which is another getter to retrieve the ID attribute
        """
        return self.ID

    def set_type(self, pokemon_type):
        """
        Creating the set_type method, which is another setter to update the pokemon_type attribute!
        """
        if type(pokemon_type) == str:
            self.type = pokemon_type
            return True
        else:
            return False

    def get_type(self):
        """
        Create the get_type method, which is another getter to retrieve the pokemon_type attribute!
        """
        return self.type

def main():
    pikachu = Pokemon("Pikachu", "Electric", 25)
    print("Name equals to: ",pikachu.get_name())
    print("ID equals to: ", pikachu.get_ID())
    print("Type equals to: ", pikachu.get_type())

    print("\nLet's change the characterisitcs of Pikachu to test the setter and getter function: \n")

    pikachu.set_ID(100)
    print("ID equals to: ", pikachu.get_ID())

    pikachu.set_type("Ground")
    print("Type equals to: ", pikachu.get_type())

    pikachu.set_name("Chifung")
    print("Name equals to: ",pikachu.get_name())

if __name__ == "__main__":
    main()

"""#### Another Set of Sample Codes to test the Setter and Getter Function"""

pikachu = Pokemon("Pikachu", "Electric", 25)

pikachu.set_ID(100)
print("ID equals to: ", pikachu.get_ID())

pikachu.set_type("Ground")
print("Type equals to: ", pikachu.get_type())

pikachu.set_name("Chifung")
print("Name equals to: ",pikachu.get_name())