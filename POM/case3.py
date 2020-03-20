import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)
from Selectors.Selectors_Class import Selector
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from JavaScript.JS_CASE3 import js_find_the_shortest_flight

class Case3():
    def __init__(self, browser):
        self.browser = browser
        one_stop = Selector.one_stop_button
        flight_enter_button = Selector.flight_enter_button
        
        one_stop = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, one_stop))).click()
        shortest_flight = self.browser.execute_script(js_find_the_shortest_flight, flight_enter_button)
    
    def test_stops(self):
        stops = Selector.stops_selector
        try:
            stops = WebDriverWait(self.browser, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, stops)))
            if len(stops) <= 4:
                return True
            else:
                return False
        except Exception as e:
            return str(e)

