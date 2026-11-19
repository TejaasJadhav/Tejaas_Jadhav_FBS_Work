class vehicles:
    def __init__(self, vehicle_type, person):
        self.vehicle_type = vehicle_type
        self.person = person

class two_wheeler(vehicles):
    def __init__(self, vehicle_type, person):
        super().__init__(vehicle_type, person)
    def calToll(self):
        if self.person>2:
            print(f"total Toll for Two wheeler is {(self.person*10)+20}")
        else:
            print(f"total Toll for Two wheeler is {20}")

class Three_wheeler(vehicles):
    def __init__(self, vehicle_type, person):
        super().__init__(vehicle_type, person)
    def calToll(self):
        if self.person>3:
            print(f"total Toll for Three wheeler is {(self.person*20)+30}")
        else:
            print(f"total Toll for Three wheeler is {30}")


class Four_wheeler(vehicles):
    def __init__(self, vehicle_type, person):
        super().__init__(vehicle_type, person)
    def calToll(self):
        if self.person>4:
            print(f"total Toll for Four wheeler is {(self.person*30)+40}")
        else:
            print(f"total Toll for Four wheeler is {40}")

class heavy_wheeler(vehicles):
    def __init__(self, vehicle_type, person):
        super().__init__(vehicle_type, person)
    def calToll(self):
        if self.person>6:
            print(f"total Toll for heavy wheeler is {(self.person*100)+30}")
        else:
            print(f"total Toll for heavy wheeler is {60}")

two=two_wheeler("Two Wheeler", 3)
three=Three_wheeler("Three Wheeler", 4)
four=Four_wheeler("Four Wheeler", 5)
heavy=heavy_wheeler("Heavy Wheeler", 7)

three.calToll()
four.calToll()
heavy.calToll()
two.calToll()