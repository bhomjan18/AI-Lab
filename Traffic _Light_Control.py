#Traffic Light Control
def lightControl(light,pedestrianbutton):
        if "red" in light :
            return "Cars must stop."
        if "green" in light :
            return "Cars must go."
        if "yellow" in light :
            return "Cars must slow down and prepare to stop."
        if  "Yes" in pedestrianbutton :
            return "The light will turn red after a short delay."
        return "Not clear criteria"

def main():
    print("Traffic Light Control")
    print("Enter the color of  traffic light and  is the pedestrian button pressed? :")
    lights = input("Light: ")
    button = input("Pedestrain button pressed or not ? (Yes or No:)")
    print(lightControl(lights,button))
main()
