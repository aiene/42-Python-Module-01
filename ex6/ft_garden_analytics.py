#!/usr/bin/env python3

class Plant:
    class _Stats:
        def __init__(self) -> None:
            self._grow_count = 0
            self._show_count = 0
            self.age_count = 0

        def display(self, name: str) -> None:
            print(f"[statistics for {name}]")
            print(f"Stats: {self._grow_count} grow, "
                  f"{self.age_count} age, {self._show_count} show")

    def __init__(self, name: str, age: int, height: float,
                 growth_rate: float) -> None:
        self.name = name
        self._height = height
        self._days_old = age
        self.growth_rate = growth_rate
        self._stats = self._Stats()

    @staticmethod
    def is_age(age: int) -> bool:
        return age > 365

    @classmethod
    def new_plant(cls) -> "Plant":
        return cls("Unknown Plant", 0, 0.0, 1.0)

    def show_stats(self) -> None:
        self._stats.display(self.name)

    def show(self) -> None:
        print(f"{self.name}: {round(self._height, 1)}cm,"
              f" {self._days_old} days old")
        self._stats._show_count += 1

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

    def grow(self) -> None:
        self._stats._grow_count += 1
        self._height += self.growth_rate

    def age(self) -> None:
        self._stats.age_count += 1
        self._days_old += 1


class Flower(Plant):
    def __init__(
            self, name: str, age: int,
            height: float, growth_rate: float, color: str) -> None:
        super().__init__(name, age, height, growth_rate)
        self.color = color
        self._bloomed = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")

    def bloom(self) -> str:
        self._bloomed = True
        return f"{self.name} is blooming beautifully!"


class Tree(Plant):
    def __init__(
            self, name: str, age: int,
            height: float, growth_rate: float,
            trunk_diameter: float = 0.0) -> None:
        super().__init__(name, age, height, growth_rate)
        self.trunk_diameter = trunk_diameter
        self.shade = 0

    def show(self) -> None:
        super().show()
        print(f" Trunk Diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        self.shade += 1
        print(f"Tree {self.name} now produces a shade of "
              f"{self._height}cm long and {self.trunk_diameter}cm wide.")

    def display(self) -> None:
        print(f"  {self.shade} shade")


class Seed(Flower):
    def __init__(
            self, name: str, age: int, height: float,
            growth_rate: float, color: str) -> None:
        super().__init__(name, age, height, growth_rate, color)

    def show(self) -> None:
        super().show()
        if self._bloomed is True:
            seeds = 42
            print("Sunflower is blooming beautifully!")
            print(f" Seeds: {seeds}")
        else:
            seeds = 0
            print("Sunflower has not bloomed yet")
            print(f" Seeds: {seeds}")


if __name__ == "__main__":
    flower = Flower("Rose", 10, 15.0, 8, "red")
    tree = Tree("Oak", 365, 200.0, 0.5, 5.0)
    seed = Seed("Sunflower", 45, 80.0, 30.0, "yellow")
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_age(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_age(400)}")
    print()
    print(f"=== {type(flower).__name__}")
    flower.show()
    print("Rose has not bloom yet")
    flower.show_stats()
    print("[asking the rose to grow and bloom]")
    flower.grow()
    flower.get_age()
    flower.show()
    print(f"{flower.bloom()}")
    flower.show_stats()
    print()

    print(f"=== {type(tree).__name__}")
    tree.show()
    tree.show_stats()
    tree.display()
    print("[asking the oak to produce shade]")
    tree.produce_shade()
    tree.show_stats()
    tree.display()

    print()
    print(f"=== {type(seed).__name__}")
    seed.show()
    print("[make sunflower grow, age and bloom]")
    seed.bloom()
    seed.grow()
    seed.age()
    seed.show()
    seed.show_stats()
    print()
    plant_n = Plant.new_plant()
    print("=== Anonymous")
    new_plant = Plant.new_plant()
    new_plant.show()
    new_plant.show_stats()
