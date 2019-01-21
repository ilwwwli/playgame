class Skill(object):
    def __init__(self, name:str, pattern:list(list), effects:dict):
        self.name = name
        self.pattern = pattern
        self.effects = effects

    def 