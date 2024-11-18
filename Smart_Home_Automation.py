#Smart Home Automation
def smart(automate,temperature):
        
        if "Dark Outside" in automate and "Someone is at home" in automate:
            return "Turn on the lights."
        
        if "Security System is armed" in automate and  "Door Opened" in automate:
            return "Sound the alarm."
        
        if  temperature is not None and  temperature < 18 :
            return "Turn on the heater."
        
        if  temperature is not None and  temperature > 25 :
            return "Turn on the air conditioner."
        
       
        
        return "Not clear criteria"

def main():

    automater =[]
    temperature = None
    
   
    print("Enter Enviroment details (type 'done' when finished):")
    while True:
        automate = input("Temperature or Environment Details: ")
        if automate == "done":
            break    
       
        try:
            temp_value = int(automate)
            temperature = temp_value 
        except ValueError:    
            automater.append(automate)
    
    
    print(smart(automater,temperature))
main()