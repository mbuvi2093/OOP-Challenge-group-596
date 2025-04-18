class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  
        self.energy = 5  
        self.happiness = 5  
        self.tricks = []  
    
    def eat(self):
        self.hunger = max(0, self.hunger - 3)  # Reduce hunger by 3, but not below 0
        self.happiness += 1  # Increase happiness by 1
        if self.happiness > 10:  # Cap happiness at 10
            self.happiness = 10
        print(f"{self.name} has eaten and is feeling better!")
    
    def sleep(self):
        self.energy = min(10, self.energy + 5)  # Increase energy by 5, but not above 10
        print(f"{self.name} had a good nap and is feeling energized!")
    
    def play(self):
        if self.energy < 2:
            print(f"{self.name} is too tired to play right now!")
            return
        
        self.energy -= 2  # Decrease energy by 2
        self.happiness += 2  # Increase happiness by 2
        if self.happiness > 10:  # Cap happiness at 10
            self.happiness = 10
        self.hunger += 1  # Increase hunger by 1
        if self.hunger > 10:  # Cap hunger at 10
            self.hunger = 10
        print(f"{self.name} had fun playing!")
    
    def get_status(self):
        print(f"\n--- {self.name}'s Status ---")
        print(f"Hunger: {self.hunger}/10 {'🍽️' * (10-self.hunger)}")
        print(f"Energy: {self.energy}/10 {'⚡' * self.energy}")
        print(f"Happiness: {self.happiness}/10 {'😊' * self.happiness}")
        
        # Status messages based on current state
        if self.hunger > 7:
            print(f"{self.name} is really hungry!")
        if self.energy < 3:
            print(f"{self.name} is getting tired...")
        if self.happiness < 3:
            print(f"{self.name} is feeling sad.")
        elif self.happiness > 7:
            print(f"{self.name} is very happy!")
    
    # Bonus methods
    def train(self, trick):
        if trick in self.tricks:
            print(f"{self.name} already knows how to {trick}!")
            return
            
        if self.energy < 3:
            print(f"{self.name} is too tired to learn new tricks right now.")
            return
            
        self.tricks.append(trick)
        self.energy -= 1
        self.happiness += 1
        if self.happiness > 10:
            self.happiness = 10
        print(f"{self.name} has learned to {trick}!")
    
    def show_tricks(self):
        if not self.tricks:
            print(f"{self.name} doesn't know any tricks yet.")
        else:
            print(f"\n{self.name}'s Tricks:")
            for i, trick in enumerate(self.tricks, 1):
                print(f"{i}. {trick}")

   
