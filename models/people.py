class Human:
	def __init__(self,
			name: str,
				 
			age: int,
			height: int,
			weight: int,
			health: int,
            intelligence: int,
			
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
		self.money = money
		self.mood = mood
		self.inventory = inventory
		self.badges = badges

class Mobster(Human):
	def __init__(self, 
			name: str,
			age: int,
			height: int,
			weight: int,
			health: int,
            intelligence: int,
				
			fighting: int,
			shooting: int,
			driving: int,
				
			stealing: int,
			stealth: int,
				
			charisma: int):
		super.__init__(name, age, height, weight, health, intelligence)
		self.fighting = fighting
		self.shooting = shooting
		self.driving = driving
		self.stealing = stealing
		self.stealth = stealth
		self.charisma = charisma

class Politician(Human):
	def __init__(self,
			name: str,
			age: int,
			height: int,
			weight: int,
			health: int,
            intelligence: int,
				
			corruption: int,
                
            charisma: int):
		super.__init__(name, age, height, weight, health, intelligence)
		self.corruption = corruption
		self.charisma = charisma

# Police != Police chief
class Police(Human):
    def __init__(self,
            name: str,
		    age: int,
		    height: int,
		    weight: int,
		    health: int,
            intelligence: int,
        
            corruption: int,
            
            fighting: int,
            shooting: int,
            driving: int):
        super.__init__(name, age, height, weight, health, intelligence)
        self.corruption = corruption
        self.fighting = fighting
        self.shooting = shooting
        self.driving = driving