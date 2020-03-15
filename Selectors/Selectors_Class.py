
class Selector():
   
    #flights
    flight_tab = "[data-name='flights']"
    inputs_main_selector = "*//div[@class='select2-container form-control']"
    results_selector = "ul.select2-results > li"

    #depart
    depart_selector = "*//div[@class='col-md-3 col-xs-12']//div[@class='form-icon-left']"
    depart_next_month = "div[class='datepicker -bottom-left- -from-bottom- active'] > nav > div[data-action='next']"
    depart_day_selector = "div[class='datepicker -bottom-left- -from-bottom- active'] > div[class='datepicker--content'] > div[class='datepicker--days datepicker--body active'] > div[class='datepicker--cells datepicker--cells-days']"
    
    #passengers
    all_passengers = "div.col-4 div.form-group.form-spin-group"

    #search button
    search_button = "div.col-xs-12.col-md-1 button" 

    #js universal
    js_universal = "div[class='datepicker -bottom-left- -from-bottom- active'] div[class='datepicker--cells datepicker--cells-days'] div"
#--------------------------
    #CASE1
    sorted_result = "button[class='btn btn-primary btn-block theme-search-results-item-price-btn']"
    sorted_flights = "p.theme-search-results-item-price-tag"

    flights_details = "div[class='theme-search-results-item-flight-section']"
    flights_points = "p[class='theme-search-results-item-flight-section-meta-city']"
#--------------------------
    #CASE2
    depart_arrival_date_time = "ul[class='booking-amount-list clearfix mb-20'] > li > span"
    total_price = "li[class='total'] > span"
    booking_details = "div[class='hotel-room-sm-item mb-30'] div:nth-child(2) h6" #// js selector
#--------------------------
    #CASE3
    one_stop_button = "label[for='1']"
    flight_enter_button = "button[class='btn btn-primary btn-block theme-search-results-item-price-btn']"
    stops_selector = "span[class='meta text-muted']"