class Animal:
    animaltype = ""
    animalvoice = ""
    instances = list()

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


    def feed(self):
        print(f"Накормлено животное: {self.animaltype} {self.name}.")

    def voice(self):
        print(f"{self.animaltype.capitalize()} {self.name} имеет голос: {self.animalvoice}.")

    def getweight(self):
        print(f"{self.animaltype.capitalize()} {self.name} имеет вес {self.weight} килограмм(а).")


class Bird(Animal):

    def geteggs(self):
        print(f"Яйца собраны: {self.animaltype} {self.name}.")


class DairyCattle(Animal):

    def getmilk(self):
        print(f"Животное подоено: {self.animaltype} {self.name}.")


class Cow(DairyCattle):
    animalvoice = "Му-у-у-у!"
    animaltype = "корова"


class Goat(DairyCattle):
    animalvoice = "Ме-ме-ме-ме!"
    animaltype = "коза"


class Sheep(Animal):
    animalvoice = "Бе-е-е-е-е!"
    animaltype = "овца"

    def cutwool(self):
        print(f"Овца {self.name} пострижена.")
        pass


class Goose(Bird):
    animalvoice = "Га-га-га!"
    animaltype = "гусь"


class Duck(Bird):
    animalvoice = "Кря-кра-кря!"
    animaltype = "утка"


class Hen(Bird):
    animalvoice = "Ко-ко-ко!"
    animaltype = "курица"



pets_dict = {
"Серый" : Goose("Серый", 7),
"Белый" : Goose("Белый", 8),
"Манька" : Cow("Манька", 426),
"Барашек" : Sheep("Барашек", 70),
"Кудрявый": Sheep("Кудрявый", 85),
"Ко-ко" : Hen("Ко-Ко", 4),
"Куквреку" : Hen("Куквреку", 5),
"Рога" : Goat("Рога", 65),
"Копыта" : Goat("Копыта", 75),
"Кряква" : Duck("Кряква", 4),
}

pets_weights = []
for pets_item in pets_dict.values():
    pets_weights.append(pets_item.weight)
print(f"Общий вес животных составляет: {sum(pets_weights)} киллограмм.")

max_pet_weight = max(pets_weights)
for pets_item in pets_dict.values():
    if pets_item.weight == max_pet_weight:
        print(f"Самое тяжелое животное: {pets_item.name}.")


#Тестируем кормление
pets_dict["Серый"].feed()

#Тестируем голос
pets_dict["Копыта"].voice()

#Тестируем доение
pets_dict["Манька"].getmilk()

#Тестируем сбор яиц
pets_dict["Серый"].geteggs()

#Тестируем стрижку
pets_dict["Барашек"].cutwool()

#Узнаём вес
pets_dict["Ко-ко"].getweight()



