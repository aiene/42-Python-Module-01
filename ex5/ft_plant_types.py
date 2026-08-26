#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, age: int, height: float,
                 growth_rate: float) -> None:
        self.name = name
        self._height = height
        self._days_old = age
        self.growth_rate = growth_rate

    def show(self) -> None:
        print(f"{self.name}: {round(self._height, 1)}cm,"
              f" {self._days_old} days old")

    def set_height(self, height: float) -> bool:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            return False
        else:
            self._height = height
            return True

    def get_height(self) -> float:
        return self._height

    def set_age(self, new_age: int) -> bool:
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative")
            return False
        else:
            self._days_old = new_age
            return True

    def get_age(self) -> int:
        return self._days_old


class Flower(Plant):
    def __init__(
            self, name: str, age: int,
            height: int, growth_rate: float, color: str) -> None:
        super().__init__(name, age, height, growth_rate)
        self.color = color

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")

    def bloom(self) -> str:
        return f"{self.name} is blooming beautifully!"


class Tree(Plant):
    def __init__(
            self, name: str, age: int,
            height: float, growth_rate: float,
            trunk_diameter: float = 0.0) -> None:
        super().__init__(name, age, height, growth_rate)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk Diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of "
              f"{self._height}cm long and {self.trunk_diameter}cm wide.")


class Vegetable(Plant):
    def __init__(
            self, name: str, age: int, height: float,
            growth_rate: float, nutritional_value: int,
            harvest_season: str) -> None:
        super().__init__(name, age, height, growth_rate)
        self.nutritional_value = nutritional_value
        self.harvest_season = harvest_season

    def show(self) -> None:
        super().show()
        print(f"Harvest Season: {self.harvest_season}")
        print(f"Nutritional Value: {self.nutritional_value}")

    def grow(self) -> None:
        self._height += self.growth_rate
        self.nutritional_value += 1

    def age(self) -> None:
        self._days_old += 1


if __name__ == "__main__":
    flower = Flower("Rose", 10, 15, 1.5, "red")
    tree = Tree("Oak", 365, 200.0, 0.5, 5.0)
    vegetable = Vegetable("Tomato", 10, 5.0, 2.1, 0, "April")
    print("=== Garden Plant Types ===")
    print(f"=== {type(flower).__name__}")
    flower.show()
    print("Rose has not bloom yet")
    print("[asking the rose to bloom]")
    flower.show()
    print(f"{flower.bloom()}")
    print()
    print(f"=== {type(tree).__name__}")
    tree.show()
    print("[asking the oak to produce shade]")
    tree.produce_shade()
    print()
    print(f"=== {type(vegetable).__name__}")
    vegetable.show()
    print("[make tomato grow and age for 20 days]")
    print(f" Nutritional Value: {vegetable.nutritional_value}")
    for i in range(20):
        vegetable.grow()
        vegetable.age()
    vegetable.show()
