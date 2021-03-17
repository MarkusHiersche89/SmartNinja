class Player():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

class BasketballPlayer(Player):
    # keine Variablen zu definieren wie in C#/Java
    x1 = 0  # public
    _x2 = 0  # private
    __x3 = 0  # protected

    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self._first_name = "abc"
        self.__first_name = "def"
        self.points = points
        self.rebounds = rebounds
        self.assists = assists

    def kg_to_lbs(self):
        punds = self.weight_kg * 2.2
        return punds


lebron = BasketballPlayer(first_name="Lebron", last_name="James", height_cm=200,
                          weight_kg=110, points=28, rebounds=10, assists=7.2)
print(type(lebron))
print(lebron.first_name)
lebron.first_name = "Alex"
print(lebron.first_name)

kevin = BasketballPlayer(first_name="Kevin", last_name="Duran", height_cm=210,
                         weight_kg=108, points=27.5, rebounds=7.1, assists=4)

list_bbplayers = [lebron, kevin]
print(type(list_bbplayers))

for p in list_bbplayers:
    print(p.first_name + " " + p.last_name)

print(lebron.kg_to_lbs())


class footballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_card):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_card = red_card

