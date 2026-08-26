#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, age: int, height: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose", 30, 25)
    sunflower = Plant("Sunflower", 45, 80)
    cactus = Plant("Cactus", 120, 15)

    rose.show()
    sunflower.show()
    cactus.show()
