import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)
from selenium import webdriver
from Selectors.Selectors_Class import Selector
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from JavaScript.JS_setup import js_flights_tab, js_current_day, js_get_month_days, js_click_day, js_cookie_dismiss

class Flights_setup():
    def __init__(self, browser):
        self.browser = browser
        self.browser.execute_script(js_cookie_dismiss)

    def click_flight_tab(self):
        try:
            flight_s = Selector.flight_tab
            self.browser.execute_script(js_flights_tab, flight_s)
        except Exception as e:
            raise("Couldn't open flight tab, "+str(e))
    
    def setup_the_directions(self):
        inputs_main_selector = Selector.inputs_main_selector
        results = Selector.results_selector
        try:
            inputs = WebDriverWait(self.browser, 10).until(EC.visibility_of_all_elements_located((By.XPATH, inputs_main_selector)))
            inputs[1].click()
            main_input = inputs[1].find_element_by_xpath("./following::input")
            main_input.send_keys("MUC")
            sleep(3)
            main_input.send_keys(Keys.ENTER)
        except Exception as e:
            raise("Couldn't setup the direction, "+str(e))

    def setup_depart(self, input):
        depart_selector = Selector.depart_selector
        depart_next_month = Selector.depart_next_month
        js_universal = Selector.js_universal
        days_to_add = input
        try:
            depart_selector = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, depart_selector)))
            depart_selector.click()
            month_days = int(self.browser.execute_script(js_get_month_days, js_universal))
            current_day = int(self.browser.execute_script(js_current_day, js_universal)) + days_to_add
            if current_day > month_days:
                while current_day > month_days:
                    next_month = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, depart_next_month)))
                    next_month.click()
                    current_day -= month_days
                    month_days = int(self.browser.execute_script(js_get_month_days, js_universal))
            day_click = self.browser.execute_script(js_click_day, current_day, js_universal)
        except Exception as e:
            raise("Couldn't setup the depart, "+str(e))
    
    def setup_passengers(self,adult,child,infant):
        all_passengers = Selector.all_passengers
        passeners_to_set = [int(adult), int(child), int(infant)]
        try:
            all_passengers = WebDriverWait(self.browser, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, all_passengers)))
            for x in range(len(all_passengers)):
                current_amount = all_passengers[x].find_element_by_css_selector("input").get_attribute("value")
                if int(current_amount) > passeners_to_set[x]:
                    decrease_button = all_passengers[x].find_element_by_xpath("*//button[contains(text(), '-')]")  
                    for y in range(int(current_amount)-passeners_to_set[x]):
                        decrease_button.click()
                else:
                    increase_button = all_passengers[x].find_element_by_xpath("*//button[contains(text(), '+')]")
                    for y in range(passeners_to_set[x]-int(current_amount)):
                        increase_button.click()
        except Exception as e:
            raise("Couldn't setup the passengers, "+str(e))
    
    def click_search(self):
        try:
            search_button = Selector.search_button
            search_button = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, search_button)))
            search_button.click()
        except Exception as e:
            raise("Couldn't click search, "+str(e))
