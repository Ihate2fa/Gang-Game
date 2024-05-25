class Mafia:
    def __init__(self):
        self.clean_money = 0
        self.dirty_money = 0

        self.members = {} # role : list of members
        self.inventory = {}
        self.relations = {}

    