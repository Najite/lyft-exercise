import unittest
from datetime import date

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindleBattery


class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = date.fromisoformat('2022-06-22')
        last_service_date = date.fromisoformat('2022-03-21')
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())
        

    def test_battery_should_not_be_serviced(self):
        current_date = date.fromisoformat('2022-06-22')
        last_service_date = date.fromisoformat('2002-03-21')
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())