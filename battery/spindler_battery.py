from battery.battery import Battery
from utils import add_years_to_date
class SpindleBattery(Battery):
    def __init(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
        
        
    def needs_service(self):
        battery_serviced_date = add_years_to_date(self.last_service_date, 2)
        if battery_serviced_date < self.current_date:
            return True
        else:
            return False
        