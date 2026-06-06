# Вариант 4.
# Создайте класс "Животное", который содержит информацию о виде и возрасте 
# животного. Создайте классы "Собака" и "Кошка", которые наследуются от класса
# "Животное" и содержат информацию о породе.


class Animal:

    def __init__(self, species: str, age: int):
        self.species = species
        self.age = age

    def get_info(self) -> str:
        return f"Вид: {self.species}, Возраст: {self.age} лет(года)"


class Dog(Animal):

    def __init__(self, age: int, breed: str):
        super().__init__(species="Собака", age=age)
        self.breed = breed

    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info}, Порода: {self.breed}"

    def bark(self) -> str:
        return "Гав-гав!"


class Cat(Animal):

    def __init__(self, age: int, breed: str):
        super().__init__(species="Кошка", age=age)
        self.breed = breed

    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info}, Порода: {self.breed}"

    def meow(self) -> str:
        return "Мяу!"


if __name__ == "__main__":
    print("--- Тестирование базового класса 'Животное' ---")
    generic_animal = Animal(species="Попугай", age=2)
    print(generic_animal.get_info())

    print("\n--- Тестирование дочернего класса 'Собака' ---")
    my_dog = Dog(age=4, breed="Немецкая овчарка")
    print(my_dog.get_info())
    print(f"Издаваемый звук: {my_dog.bark()}")

    print("\n--- Тестирование дочернего класса 'Кошка' ---")
    my_cat = Cat(age=3, breed="Сиамская")
    print(my_cat.get_info())
    print(f"Издаваемый звук: {my_cat.meow()}")

