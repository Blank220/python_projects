import random

class Pick:
    def batch(self):
        batch_choose = random.randint(1,2)
        print(batch_choose)
    
    def program(self):
        choose2 = random.randint(1,10)
        print(choose2)

choose = Pick()
choose.batch()
choose.program()
        