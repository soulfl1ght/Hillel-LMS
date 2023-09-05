class Godzilla:
    def __init__(self, stomach_capacity):
        self.stomach_capacity = stomach_capacity
        self.current_stomach_capacity = 0 

    def eat(self, human_volume):
        if self.current_stomach_capacity + human_volume <= self.stomach_capacity:
            self.current_stomach_capacity += human_volume
            print(f"Godzilla з'їв людину об'ємом {human_volume}.")
            
            
            if self.current_stomach_capacity / self.stomach_capacity > 0.9:
                print("Godzilla вже наївся і не може з'їсти більше людей.")
        else:
            print("Godzilla не може з'їсти цю людину, бо шлунок заповнений.")

godzilla = Godzilla(stomach_capacity=1000)

godzilla.eat(300)
godzilla.eat(400)
godzilla.eat(350)
godzilla.eat(200)
