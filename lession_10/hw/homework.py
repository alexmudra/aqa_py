from random import randint, choice

heroes = {
            "Котигорошко": {"power": 50,
                            "shield": 10,
                            "helth": 100,
                            "home": "поле",
                            "side": "heroes",
                            "friends": None
                            },
            "Помор": {"power": 30,
                            "shield": 20,
                            "helth": 100,
                            "home": "берег",
                            "side": "heroes",
                            "friends": None
                            },
            "Вернигора": {"power": 60,
                            "shield": 0,
                            "helth": 100,
                            "home": "гори",
                            "side": "heroes",
                            "friends": None
                            },
            }

neutrals = {
            "Кінь": {"power": 5,
                            "shield": 20,
                            "helth": 100,
                            "home": "поле",
                            "side": "neutrals",
                            "friends": None
                            },
            "Морський Вовк": {"power": 10,
                            "shield": 10,
                            "helth": 100,
                            "home": "берег",
                            "side": "neutrals",
                            "friends": None
                            },
            "Грізлі": {"power": 20,
                            "shield": 0,
                            "helth": 100,
                            "home": "гори",
                            "side": "neutrals",
                            "friends": None
                            },
            }

darks = {
            "Польовик": {"power": 10,
                            "shield": 50,
                            "helth": 50,
                            "home": "поле",
                            "side": "darks",
                            "friends": None
                            },
            "Водяник": {"power": 20,
                            "shield": 30,
                            "helth": 70,
                            "home": "берег",
                            "side": "darks",
                            "friends": None
                            },
            "Печерник": {"power": 20,
                            "shield": 0,
                            "helth": 100,
                            "home": "гори",
                            "side": "darks",
                            "friends": None
                            },
            }

locations = [
            "дорога", "поле", "берег", "гори"
            ]

actions = [
           "розійтися", "дружити", "битися"
          ]

def select_player():
    """Вибір з списку позитивних персонажів"""
    # Завдання - додати можливість обирати також зі списку
    # негативних персонажів
    char_list = [h for h in heroes]
    select = input(f"Оберіть персонажа: {', '.join([h for h in heroes])}: ").capitalize()
    if select not in char_list:
        print(f"Персонажа {select} немає спробуйте ще раз")
        return select_player()
    player = heroes.pop(select)
    return player


def select_locations():
    return choice(locations)

def select_enemy():
    """Компютер робить вибір з списку залишившихся персонажів"""
    # Завдання - додати можливість  зі списку
    # нейтралів обирати персонаж компютеру
    enemy_1 = choice(heroes)
    enemy_2 = choice(darks)
    #enemy_3 = choice(neutrals)
    number = randint(1, 2)
    if number == 1:
        enemy = heroes.pop(enemy_1)
        return enemy
    else:
        enemy = enemy_2.pop(enemy_2)
        return enemy

def meet_hero_and_enemy(player, enemy):
    if player["side"] == enemy["side"] or enemy["side"] == "neutrals":
        actions = (0, 1)
    else:
        actions = (0, 2)
    return actions



def game():
    player = select_player()
    print(player)

if __name__ == "__main__":
    game()