
js_get_number_of_all_results = """
    const all_results = document.querySelectorAll(arguments[0])
    return all_results.length
"""

js_check_if_sorted = """
    const first_s = arguments[0]
    function sort_check(first){
        var all_prices = document.querySelectorAll(first)
        var previous_price = 0;
        var result = null
        for(x=0;x<all_prices.length;x++){
            const price = parseInt(String(all_prices[x].innerText).slice(4))
            if(previous_price==0){
                previous_price = price
            }
            else{
                if(price < previous_price){
                    result = false
                    break
                }
                else{
                    result = true
                    previous_price = price
                }
            }
        }
        return result
    }
    return sort_check(first_s)
"""

js_check_points = """
    const first_s = arguments[0];
    const second_s = arguments[1];
    function check_points(first, second){
        const all_results = document.querySelectorAll(first)
        const nyc_points = ["EWR", "JFK", "LGA","SWF"]
        var result = null
        for(x=0;x<all_results.length;x++){
            const points = all_results[x].querySelectorAll(second)
            const starting_point = points[0].innerText
            const end_point = points[1].innerText
            if(nyc_points.includes(starting_point) || end_point == "MUC"){
                result = true
            }
            else{
                result = false
                break
            }
        }
        return result
    }
    return check_points(first_s, second_s)
"""