#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, age: int,
                 height: float, growth_rate: float) -> None:
        self.name = name
        self.days_old = age
        self.height = height
        self.growth_rate = growth_rate

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm,"
              f" {self.days_old} days old")

    def grow(self) -> None:
        self.height += self.growth_rate

    def age(self) -> None:
        self.days_old += 1


if __name__ == "__main__":
    rose = Plant("Rose", 30, 25, 0.8)
    sunflower = Plant("Sunflower", 45, 80, 0.5)
    cactus = Plant("Cactus", 120, 15, 0.1)
    plants = [rose, sunflower, cactus]
    print("=== Garden Plant Growth ===")
    for plant in plants:
        print(plant.name)
        starting_height = plant.height
        for day in range(1, 8):
            plant.grow()
            plant.age()
            print(f"=== Day {day} ===")
            plant.show()
            print()
        total_growth = plant.height - starting_height
        print(f"Growth this week: {round(total_growth, 1)}cm")
