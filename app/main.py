from ai_services import get_meal_analysis



print("AI Meal Analyzer")

def get_meal_description():

    meal_description = input("Describe your meal:").strip()


    while meal_description == "":
        print("Please enter a meal description")

        meal_description = input("Describe your meal:").strip()

    return meal_description

meal_description = get_meal_description()

meal_analysis = get_meal_analysis(meal_description)


print(f"You entered: {meal_description}")
print(meal_analysis)
        