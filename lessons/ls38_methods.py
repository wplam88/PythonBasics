"""An example of methods and method calls"""

class Person: 
    """A model of a Person"""
    name: str
    age: int = 0

    def __init__(self, name: str):
        """Constructor of Person initializes name"""
        self.name = name

    def say_hello(self) -> None:
        """Greet the user!"""
        print(f"Hello, I'm {self.name}!")

def main() -> None:
    """Entrypoint."""
    person_a = Person("Will")
    person_a.say_hello()

    person_b = Person("Guillermo")
    person_b.say_hello()
    
if __name__ == "__main__":
    main()