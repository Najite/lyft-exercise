import unittest
from datetime import date

from battery.spindler_battery import SpindleBattery

class TestSpindlerBattery(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_date = date.fromisoformat('2022-06-22')
        last_service_date = date.fromisoformat('2022-03-21')
        battery = SpindleBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())
        

    def test_engine_should_not_be_serviced(self):
        current_date = date.fromisoformat('2022-06-22')
        last_service_date = date.fromisoformat('2019-03-21')
        battery = SpindleBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())
