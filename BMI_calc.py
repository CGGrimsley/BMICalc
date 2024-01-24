# BMI Calculator made for funsies
def bmi_calculator():
    bmi_tracker = []

    while True:
        calc = input("Would you like to calculate your BMI? (y/n)")
        if calc.lower() == "y":
            try:
                height = int(input("Enter your height in inches"))
                weight = int(input("Enter your weight in pounds"))
                bmi = (weight / (height ** 2)) * 703
                bmi = round(bmi, 2)
                print("Your bmi is ", bmi)
                print("Underweight = <18.5", "Healthy Weight = 18.5 - 24.9")
                print("Overweight = 25-29.9", "Obese = 30 or higher")

                match bmi:
                    case bmi if bmi < 18.5:
                        print("Your bmi would indicate you are Underweight.")
                    case bmi if 18.5 <= bmi < 25:
                        print("Your bmi would indicate you are a Healthy Weight, Congratulations!")
                    case bmi if 25 <= bmi < 30:
                        print("Your bmi would indicate you are Overweight.")
                    case _:
                        print("Your bmi would indicate you are Obese.")

                keep = input("would you like add this BMI to your tracker? (y/n)").lower()
                match keep:
                    case "y":
                        bmi_tracker.append(bmi)
                        print("This BMI will be added to your tracker!")
                    case "n":
                        print("This BMI will not be added to your tracker!")
                    case _:
                        print("Invalid input please try again.")

                if len(bmi_tracker) > 0:
                    print("Your tracked BMI values:", bmi_tracker)

            except ValueError:
                print("Invalid input, please try again.")
        elif calc.lower() == "n":
            track = input("Would you like to view your tracked BMIs? (y/n)").lower()
            match track:
                case "y":
                    print("Your tracked BMI values:", bmi_tracker)
                case "n":
                    exit_app = input("Would you like to exit the application? (y/n)").lower()
                    if exit_app == "y":
                        print("Goodbye!")
                        break
                    elif exit_app == "n":
                        continue
                    else:
                        print("Invalid input, please try again.")
        else:
            print("Invalid input, please try again.")


bmi_calculator()
