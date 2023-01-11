from tires.tires import Tires


class CarriganTires(Tires):
    def __init__(self, tire_wears):
        self.tire_wears = tire_wears
        
        
    def needs_service(self):
        if self.tire_wears >= 0.9:
            return True
        return False