class Animal:
  def __init__(self, name, weight, voice):
    self.name = name
    self.weight = weight #kg
    self.voice = voice
  def feed(self):
    return "I fed %s." % self.name
  def say(self):
    return "This animal says %s." % self.voice

class Birds(Animal):
  def action(self):
    return "I'm collecting eggs."

class Cattle(Animal):
  def action(self):
    return "I'm milking %s." % self.name

class Sheep(Cattle):
  def action(self):
    return "I'm shearing %s." % self.name

#Farm Animals:
white_goose = Birds("Белый", 3.3, 'Hhonk-honk')
grey_goose = Birds("Серый", 2.5, 'Hhonk-honk')
cow = Cattle("Манька", 720, 'Moo')
sheep_barashek = Sheep("Барашек", 70, 'Baa')
sheep_kudryavy = Sheep("Кудрявый", 90, 'Baa')
chicken_koko = Birds("Ко-Ко", 1, 'Cluck')
chicken_kukareku = Birds("Кукареку", 2, 'Cluck')
goat_roga = Cattle("Рога", 70, 'Maaa')
goat_koputa = Cattle("Копыта", 80, 'Maaa')
duck = Birds("Кряква", 1.6, 'Quack')

all_animals = [white_goose, grey_goose, cow, sheep_barashek, sheep_kudryavy, chicken_koko, chicken_kukareku, goat_roga, goat_koputa, duck]

for duty in all_animals:
  print(duty.feed(), duty.action(), duty.say())


print(f'\nОбщий вес животных на ферме - {round(sum([x.weight for x in all_animals]),2)} кг.')
print(f'Самое тяжелое животное на ферме весит {max([x.weight for x in all_animals])} кг.')