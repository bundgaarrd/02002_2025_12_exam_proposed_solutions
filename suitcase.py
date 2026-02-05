# Opgave 9 (Suitcase)

class Suitcase():
    
    def __init__(self, weight_limit):
        self.weight_limit = weight_limit
        self.packed_weight = 0
        self.items = [] # Could create a dictionary to keep track of item weights
        pass

    def pack_item(self, item, weight):
        if self.packed_weight + weight <= self.weight_limit:
            self.packed_weight += weight
            self.items.append(item)
            return True
        else: 
            return False

    def __add__(self, other):
        # Scuffed method, not recommended for larger classes
        new_suitcase = Suitcase(self.weight_limit + other.weight_limit)
        new_suitcase.packed_weight = other.packed_weight + self.packed_weight
        for item in self.items:
            new_suitcase.items.append(item)
        for item in other.items:
            new_suitcase.items.append(item)
        return new_suitcase

    def currently_packed(self, ):
        return self.items

# carry_on = Suitcase(7.0)
# check_in = Suitcase(23.0)
# print(carry_on.pack_item("Laptop", 1.5))
# print(check_in.pack_item("Clothes", 5.0))
# print(check_in.pack_item("E-bike", 20.0))

# all_luggage = carry_on + check_in

# print(all_luggage.currently_packed())
# # print(carry_on.currently_packed())