class Human:
	def __init__(self,
			name: str, 
			age: int,
			height: int,
			weight: int,
			health: int,
            intelligence: int,
			location: str,
			money: int,
			mood: list,
			inventory: list,
			badges: dict):
		self.name = name
		self.age = age
		self.height = height
		self.weight = weight
		self.health = health
		self.intelligence = intelligence
		self.location = location
		self.money = money
		self.mood = mood
		self.inventory = inventory
		self.badges = badges

		"""
		Badges

		Cooker - 5% faster drug production per level
		Contract Killer - 5% better chance of killing on a hitman job
		Launder - 2 days faster per level
		Master Scout - 5% boost to recruiting
		"""

class Mobster(Human):
	def __init__(self, 
			affiliation: str,
				
			fighting: int,
			shooting: int,
			driving: int,
				
			stealing: int,
			stealth: int,
				
			charisma: int,
			
			*args, 
            **kwargs):
		super.__init__(*args, **kwargs)
		self.affiliation = affiliation
		self.fighting = fighting
		self.shooting = shooting
		self.driving = driving
		self.stealing = stealing
		self.stealth = stealth
		self.charisma = charisma

class Politician(Human):
	def __init__(self,
			corruption: int,
                
            charisma: int,
			
			*args, 
            **kwargs):
		super.__init__(*args, **kwargs)
		self.corruption = corruption
		self.charisma = charisma

# Police != Police chief
class Police(Human):
    def __init__(self,
            corruption: int,
            
            fighting: int,
            shooting: int,
            driving: int,
			
			*args, 
            **kwargs):
        super.__init__(*args, **kwargs)
        self.corruption = corruption
        self.fighting = fighting
        self.shooting = shooting
        self.driving = driving