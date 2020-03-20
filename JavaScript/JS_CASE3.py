js_find_the_shortest_flight = """
    const first_s = arguments[0]
    function fastest_flight(button_s){
        all_flights = document.querySelectorAll("form[class='row']")
        var previous = 0;
        var element = "";
        for(x=0;x<all_flights.length;x++){
            const raw_text = String(all_flights[x].querySelector("div[class='theme-search-results-item-flight-section-path-fly-time']").innerText)
            var hour = raw_text.split(" ")
            const button = all_flights[x].querySelector(button_s)
            var slicer = 2
            if(hour[2].length == 1){
                slicer = 1
            }
            hour[2] = hour[2].slice(0,slicer)
            if(previous == 0){
                previous = hour[2]
                element = button
            }
            else{
                if(hour[2] < previous){
                    previous = hour[2]
                    element = button
                }
            }
        }
        element.click()
    }
    fastest_flight(first_s)
"""
