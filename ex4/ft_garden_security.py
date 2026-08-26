#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, age: int,
                 height: float, growth_rate: float) -> None:
        self.name = name
        self._days_old = 0
        self._height = 0.0
        self.growth_rate = growth_rate
        self.set_age(age)
        self.set_height(height)
        self.leaves = 5

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

    def show(self) -> None:
        print(f"{self.name}: {round(self._height, 1)}cm,"
              f" {self._days_old} days old")

    def grow(self) -> None:
        self.set_height(self._height + self.growth_rate)

    def age(self) -> None:
        self.set_age(self._days_old + 1)


if __name__ == "__main__":
    rose = Plant("Rose", 10, 15, 0.8)

    plants = [rose]
    print("=== Garden Security System ===")
    print("Plant created: ", end="")
    rose.show()
    print()
    print(f"Height updated: {rose.get_height()}cm")
    print(f"Age updated: {rose.get_age()} days")
    if rose.set_height(25):
        print(f"Height updated: {round(rose.get_height(), 1)}cm")
    else:
        print("Height update rejected")
    if rose.set_age(30):
        print(f"Age updated: {round(rose.get_age())} days")
    else:
        print("Age update rejected")
    print()
    print("Current State:", end="")
    rose.show()
