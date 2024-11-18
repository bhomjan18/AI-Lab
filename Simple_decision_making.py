from datetime import datetime

def make_decision(time, day_of_week, weather):
    current_time = datetime.strptime(time, "%H:%M").time()
    if current_time >= datetime.strptime("06:00", "%H:%M").time() and current_time <= datetime.strptime("08:00", "%H:%M").time() and day_of_week in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        return "Time to go to work."
    if current_time >= datetime.strptime("12:00", "%H:%M").time() and current_time <= datetime.strptime("13:00", "%H:%M").time():
        return "Time for lunch."
    if current_time >= datetime.strptime("21:00", "%H:%M").time() and current_time <= datetime.strptime("22:00", "%H:%M").time():
        return "Time to go to bed."
    if day_of_week in ["Saturday", "Sunday"] and weather == "sunny":
        return "Go for a walk."
    return "No specific action at this time."

def main():
    time = input("Enter the current time (HH:MM): ")
    day_of_week = input("Enter the day of the week: ").capitalize()
    weather = input("Enter the weather (sunny/cloudy/rainy/etc.): ").lower()
    decision = make_decision(time, day_of_week, weather)
    print(decision)
main()
