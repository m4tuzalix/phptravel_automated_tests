import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)
from Selectors.Selectors_Class import Selector
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

class Case2():
    def __init__(self, browser):
        self.browser = browser
    
    def test_depart_date(self, time, date):
        depart_selector = Selector.depart_arrival_date_time
        try:
            depart_date = datetime.strptime(date, "%A %d %b %Y").date()
            depart_time = time
            depart = str(depart_date)+" "+str(depart_time)
            depart_selector = WebDriverWait(self.browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, depart_selector)))
            if depart_selector[0].text == depart:
                return True
            else:
                return False
        except Exception as e:
            return str(e)
    
    def test_arrival_time(self, time, date):
        arrival_selector = Selector.depart_arrival_date_time
        try:
            arrival_date = datetime.strptime(date, "%A %d %b %Y").date()
            arrival_time = time
            arrival = str(arrival_date)+" "+str(arrival_time)
            arrival_selector = WebDriverWait(self.browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, arrival_selector)))
            if arrival_selector[1].text == arrival:
                return True
            else:
                return False
        except Exception as e:
            return str(e)

    def test_total_price(self, price):
        total_price = Selector.total_price
        try:
            total_price = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, total_price)))
            if price in total_price.text:
                return True
            else:
                return False
        except Exception as e:
            return str(e)
    
    def test_booking_details(self, place_from, place_to):
        booking_details = Selector.booking_details
        try:
            booking_details = WebDriverWait(self.browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, booking_details)))
            if f"From: {place_from}" in booking_details[0].text:
                    if f"To: {place_to}" in booking_details[1].text:
                        return True
                    else:
                        return False
            else:
                return False
        except Exception as e:
            return str(e)
