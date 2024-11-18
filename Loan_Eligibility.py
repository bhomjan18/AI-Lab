#Loan Eligibility
def eligibility(detail,age):
        if "Criminal record" in detail:
            return "Not eligible for a loan."
        if "Loan before" in detail:
           return "Not eligible for a loan."
        if  "Credit Score above 700" in detail:
            return "Eligible for Loan"
        if age >= 18 and age <= 65 and "Stable income" in detail:
            return "Eligible for Loan"
        return "Not clear criteria"

def main():
    details =[]
    age = None
    print(" Eligibility for Loan:")
    print("Age between 18 & 65")
    print("Stable income")  
    print("Credit Score above 700")
    print("Criminal Record")
    print("Loan Before")
    print("Enter applicant's details (type 'done' when finished):")
    while True:
        detail = input("Details: ")
        if detail == "done":
            break    
        try:
            temp_value = int(detail)
            age = temp_value 
        except ValueError:    
            details.append(detail)
    print(eligibility(details,age))
main()
