import unittest
import os, sys
from selenium import webdriver
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)
from POM.tests_setup import Flights_setup
from POM.case1 import Case1
import HtmlTestRunner

class Case1Test(unittest.TestCase):
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
        try:
            setup.click_flight_tab()
            setup.setup_the_directions()
            setup.setup_depart(departure_days_to_add)
            setup.setup_passengers(adults,child,infant)
            setup.click_search()
        except Exception as e:
            print(str(e))

    def test00_results_amount(self):
        case = Case1(self.driver)
        results = case.test_amount_of_results()
        self.assertEqual(results, 50)
    
    def test01_price_sorted_ascending(self):
        case = Case1(self.driver)
        sorted_correct = case.test_if_sorted_ascending()
        self.assertEqual(sorted_correct, True)

    def test02_start_end_points(self):
        case = Case1(self.driver)
        points = case.test_start_end_points()
        self.assertEqual(points, True)
        
    @classmethod
    def tearDownClass(finish):
        finish.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=os.pardir+"/Reports"))
