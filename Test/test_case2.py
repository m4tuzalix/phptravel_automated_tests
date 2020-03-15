import unittest
import os, sys
from selenium import webdriver
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)
from POM.tests_setup import Flights_setup
from POM.case2 import Case2
from JavaScript.JS_CASE2 import js_flight_data
import HtmlTestRunner

class Case2Test(unittest.TestCase):
    @classmethod
    def setUpClass(start):
        start.driver = webdriver.Chrome("chromedriver.exe")
        start.driver.set_script_timeout(20)
        start.driver.implicitly_wait(10)
        start.driver.get("https://www.phptravels.net/home")
        start.driver.maximize_window()
        
        #data for setup
        departure_days_to_add = 14 #// number symbolizes days which will be added to the current date. In this case it's gonna be 2 weeks (14 days from today)
        adults = 2 #// number of adults passengers
        child = 2 #// number of child passengers
        infant = 0 #// mumber of infant passengers

        setup = Flights_setup(start.driver)
        case2 = Case2(start.driver)
        try:
            setup.click_flight_tab()
            setup.setup_the_directions()
            setup.setup_depart(departure_days_to_add)
            setup.setup_passengers(adults,child,infant)
            setup.click_search()
            start.data = start.driver.execute_script(js_flight_data) #// gathers data about the flight
            start.data["main"]["enter_button"].click() #// click the booking button
        except Exception as e:
            print(str(e))

    def test00_depart_time(self):
        case2 = Case2(self.driver)
        time = self.data["main"]["flight_times"][0]
        date = self.data["main"]["flight_dates"][0]
        correct_time = case2.test_depart_date(time,date)
        self.assertTrue(correct_time)
    
    def test01_arrival_time(self):
        case2 = Case2(self.driver)
        time = self.data["main"]["flight_times"][1]
        date = self.data["main"]["flight_dates"][1]
        correct_time = case2.test_arrival_time(time,date)
        self.assertTrue(correct_time)

    def test02_total_price(self):
        case2 = Case2(self.driver)
        price = self.data["main"]["flight_price"]
        correct_price = case2.test_total_price(price)
        self.assertTrue(correct_price)

    def test003_booking_details(self):
        case2 = Case2(self.driver)
        place_from = "New York"
        place_to = "Munich"
        correct_details = case2.test_booking_details(place_from, place_to)
        self.assertTrue(correct_details)

    @classmethod
    def tearDownClass(finish):
        finish.driver.quit()
    
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=os.pardir+"/Reports"))
