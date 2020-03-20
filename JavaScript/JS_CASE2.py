js_flight_data = """
    function flight_data_gather(){
        const all_flights = document.querySelectorAll("form.row")
        const random_flight = Math.floor(all_flights.length * Math.random())
       
        const flight_details = all_flights[random_flight].querySelector("div[class='theme-search-results-item-flight-section']")
        const flight_times = flight_details.querySelectorAll("p.theme-search-results-item-flight-section-meta-time")
        const flight_airline = flight_details.querySelector("h5.theme-search-results-item-flight-section-airline-title").innerText
        const flight_dates = flight_details.querySelectorAll("p.theme-search-results-item-flight-section-meta-date")
        const flight_price = all_flights[random_flight].querySelector("input[name='flight_price']").getAttribute("value")
        const enter_button = all_flights[random_flight].querySelector("button[class='btn btn-primary btn-block theme-search-results-item-price-btn']")

        const main_json = {"main":{
            "flight_times":Array.from(flight_times, time => time.innerText),
            "flight_dates":Array.from(flight_dates, date => date.innerText),
            "flight_airline":flight_airline,
            "flight_price":flight_price,
            }
        }   
        enter_button.click()
        return main_json
    }
    return flight_data_gather()
"""
