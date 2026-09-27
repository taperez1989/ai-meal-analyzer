from app.ai_services import get_meal_analysis





def get_meal_description():

    meal_description = input("Describe your meal:").strip()


    while meal_description == "":
        print("Please enter a meal description")

        meal_description = input("Describe your meal:").strip()

    return meal_description



def main():
    print("AI Meal Analyzer")

    meal_description = get_meal_description()

    meal_analysis = get_meal_analysis(meal_description)


    print(f"You entered: {meal_description}")
    print("AI Meal Analysis")
    print(f"Meal: {meal_analysis.name}")
    print(f"Estimated calories: {meal_analysis.estimated_calories} kcal")
    print(f"Protein: {meal_analysis.protein_grams} g")
    print(f"Carbohydrates: {meal_analysis.carbohydrate_grams} g")
    print(f"Fat: {meal_analysis.fat_grams} g")

if __name__ == "__main__":
    main()