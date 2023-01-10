from battery.battery import Battery
from datetime import date

class SpindleBattery(Battery):
    def __init(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
        
        
    def needs_service(self):
        battery_serviced_date = date(self.last_service_date)
        if battery_serviced_date < self.current_date:
            return True
        else:
            return False
        