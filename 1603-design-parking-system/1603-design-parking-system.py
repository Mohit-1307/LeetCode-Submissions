class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.slots = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        index = carType - 1

        if self.slots[index] > 0:
            self.slots[index] -= 1
            return True

        return False