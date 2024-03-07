class BackPack:

    laptop_size = "14 inch"

    def __init__(self, color):
        self.laptop_size = BackPack.laptop_size
        self.items = []
        self.color = color
        self.__brand = "Samsonite" # Name mangling, you shouldn't access/modify this attribute
        self._model = "BackPack" # should not access this attribute outside the class as this is protected

    # def get_brand(self):
    #     return self.__brand

    # def set_brand(self, brand):
    #     if isinstance(brand, str) and brand.isalpha():
    #         self.__brand = brand
    #         print(f"new brand name is {self.__brand}")
    #     else:
    #         print("Invalid name for brand")

    # brand = property(get_brand, set_brand)


    ## Property Decorator

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, new_brand):
        if isinstance(new_brand, str) and new_brand.isalpha():
            self.__brand = new_brand
            print(f"new brand name is {self.__brand}")
        else:
            print("Invalid Value")

my_backpack = BackPack("Black")
BackPack.laptop_size = "16 inch"
print(my_backpack.laptop_size)

your_backpack = BackPack("White")
print(your_backpack.laptop_size)

# print(your_backpack._BackPack__brand) # Acces Name Mangling attribute you shouldn't access/modify this attribute
print(my_backpack.brand)
my_backpack.brand = "Joop"
