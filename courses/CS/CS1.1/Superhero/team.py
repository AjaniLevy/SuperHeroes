class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()
    def remove_hero(self, name):
        '''Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        # if we looped through our list and did not find our hero,
        # the indicator would have never changed, so return 0
        if not foundHero:
            return 0
    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)
    def add_hero(self, hero):
        self.heroes.append(hero)
    