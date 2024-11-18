def weather(forecasts):
    if "cloudy" in forecasts and "no wind" in forecasts:
        return "It might rain."
    
    if forecasts < 0 in forecasts and "sky is clear" in forecasts:
        return "It might snow."
    
    if forecasts > 30  in forecasts and "no wind" in forecasts:
        return "It might be a hot day."
    
    if "sky is clear" in forecasts and "is wind" in forecasts:
        return "It might be a pleasant day."
    
    return "Not clear criteria"

def main():
    forecasts =[]
    print("Available Forecasts:")
    print("cloudy")
    print("no wind")
    print("temperature below 0")
    print("sky is clear")
    print("temperature above 30")
    print("is wind \n")
    print("Enter your forecast: (Type 'done' if finished)")
    while True:
        forecast =input("Forecast: ")
        if forecast == "done":
             break
        forecasts.append(forecast)
        
    print(weather(forecasts))
main()
    
    