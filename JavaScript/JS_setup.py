js_flights_tab = """
    const flights_s = arguments[0];
    const flight_tab = document.querySelector("a"+flights_s)
    flight_tab.click()
"""
js_current_day = """
    const first_s = arguments[0]
    function get_day(first){
        const all_days = document.querySelectorAll(first)
        var month_day = "";
        for(x=0;x<all_days.length;x++){
            const current_day = all_days[x].getAttribute("class")
            if(current_day.includes("current")){
                month_day = all_days[x].innerText
                break
            }
        }
        return month_day
    }
    return get_day(first_s)
"""
js_get_month_days = """
    const first_s = arguments[0];
    function get_month_days(first){
        const months = document.querySelectorAll(first)
        var final = "";
        for(x=0;x<months.length;x++){
            const day = months[x].getAttribute("data-date")
            if(day == "31" || day == "30"){
                final = day
            }
        }
        return final
    }
    return get_month_days(first_s)
"""

js_click_day = """
    const day_number = arguments[0];
    const second_s = arguments[1];
    function click_day(input, second){
        const months = document.querySelectorAll(second)
        for(x=0;x<months.length;x++){
            const day = months[x].getAttribute("class")
            if(day == "datepicker--cell datepicker--cell-day" || day == "datepicker--cell datepicker--cell-day -weekend-"){
                const number = months[x].getAttribute("data-date")
                if(number == input){
                    months[x].click()
                    break
                }
            }
        }
        
    }
    click_day(day_number, second_s)
"""

