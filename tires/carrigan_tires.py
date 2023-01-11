from tires.tires import Tires


class CarriganTires(Tires):
    def __init__(self, wears):
        self.wears = wears
        
        
    def needs_service(self):
        if self.wears >= 0.9:
            return True
        else: 
            return False