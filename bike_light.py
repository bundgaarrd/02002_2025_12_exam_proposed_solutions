# Opgave 8 (Bike Light)

class BikeLight():
    
    def __init__(self, ):
        self.mode = "off"

    def long_press(self, ):
        if self.mode == "off":
            self.mode = "weak"
        else:
            self.mode = "off"

        return self.mode

    def short_press(self, ):
        if self.mode == "off":
            pass
        elif self.mode == "weak":
            self.mode = "strong"
        elif self.mode == "strong":
            self.mode = "flash"
        elif self.mode == "flash":
            self.mode = "weak"
        
        return self.mode

# --- TEST ---
# light = BikeLight()
# print(light.long_press())
# print(light.short_press())
# print(light.short_press())
# print(light.long_press())
# print(light.long_press())