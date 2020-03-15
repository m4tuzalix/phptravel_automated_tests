import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)
from Selectors.Selectors_Class import Selector
from JavaScript.JS_CASE1 import js_get_number_of_all_results, js_check_if_sorted, js_check_points


class Case1():
    def __init__(self, browser):
        self.browser = browser

    def test_amount_of_results(self):
        results = Selector.sorted_result
        try:
            found_flights_number = self.browser.execute_script(js_get_number_of_all_results, results)
            return found_flights_number
        except Exception as e:
            return str(e)
    
    def test_if_sorted_ascending(self):
        sorted_selector = Selector.sorted_flights
        try:
            sorted_correct = self.browser.execute_script(js_check_if_sorted, sorted_selector)
            if sorted_correct != False and sorted_correct != None:
                sorted_correct = True
            else:
                sorted_correct = False
            return sorted_correct
        except Exception as e:
            return str(e)
    
    def test_start_end_points(self):
        flight_details = Selector.flights_details
        flight_points = Selector.flights_points
        try:
            final_points = self.browser.execute_script(js_check_points, flight_details, flight_points)
            if final_points != False and final_points != None:
                final_points = True
            else:
                final_points = False
            return final_points
        except Exception as e:
            return str(e)