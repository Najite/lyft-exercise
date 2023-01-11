from tires.tires import Tires


class Octoprime(Tires):
    def __init__(self, wears):
        self.wears = wears
        
    
    def needs_service(self):
        if self.wears >= 3:
            return True
        else:
            return False