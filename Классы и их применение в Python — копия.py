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
        print(f"{self.animaltype.capitalize()} {self.name} имеет вес {self.weight} килограмм.")


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


goose1 = Goose("Серый", 7)
goose2 = Goose("Белый", 8)
cow1 = Cow("Манька", 426)
sheep1 = Sheep("Барашек", 70)
sheep2 = Sheep("Кудрявый", 85)
hen1 = Hen("Ко-Ко", 4)
hen2 = Hen("Куквреку", 5)
goat1 = Goat("Рога", 65)
goat2 = Goat("Копыта", 75)
duck1 = Duck("Кряква", 4)

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
        print(pets_item.name)

# Тестируем кормление
goose1.feed()
goose2.feed()
cow1.feed()
sheep1.feed()
sheep2.feed()
hen1.feed()
hen2.feed()
goat1.feed()
goat2.feed()
duck1.feed()


#Тестируем голос
goose1.voice()
goose2.voice()
cow1.voice()
sheep1.voice()
sheep2.voice()
hen1.voice()
hen2.voice()
goat1.voice()
goat2.voice()
duck1.voice()

#Тестируем доение
cow1.getmilk()
goat1.getmilk()
goat2.getmilk()

#Тестируем сбор яиц
goose1.geteggs()
goose2.geteggs()
hen1.geteggs()
hen2.geteggs()
duck1.geteggs()

#Тестируем стрижку
sheep1.cutwool()
sheep2.cutwool()

#Узнаём вес
goose1.getweight()
goose2.getweight()
cow1.getweight()
sheep1.getweight()
sheep2.getweight()
hen1.getweight()
hen2.getweight()
goat1.getweight()
goat2.getweight()
duck1.getweight()


