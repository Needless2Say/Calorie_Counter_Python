# import libraries
import os
import json

#==================================================================================================================================
# Calorie Counter Class


class CalorieCounter:
    # Data Structures
 
    # All Nutrition Fact Labels and amount eaten today
    all_food_content = dict()

    # Units for all Nutrition Facts
    all_food_content_units = dict()

    # food info dictionary containing each individual food dictionary that has all info related to each food
    all_food_data = dict()

#==================================================================================================================================
    # Functions

    # fill all_food_content, all_food_content_amount, and all_food_content_units with nutrition facts related info
    def fill_lists(self):
        # open nutrition_facts_units json and fill following lists:
        # all_food_content[], all_food_content_amount[], and all_food_content_units[]
        file = open("nutrition_facts_units.json", 'r')

        # load json file
        json_file = json.load(file)

        # close file
        file.close()

        # loop through dictionary
        for label, units in json_file.items():
            # add label to all_food_content list
            self.all_food_content[label] = 0

            # add units to all_food_content_units
            self.all_food_content_units[label] = units

    # fill dictionary all_food_data from food in folder to_input/food
    def fill_dicts(self):
        # open directory where all foods are stored
        os.chdir("To_Input\\Foods")

        # loop through all food files in directory
        for filename in os.listdir():
            # open file
            file = open(filename, 'r')

            # read json file
            food_dict = json.load(file)

            # close file
            file.close()

            # add food_dict to all_food_data dict
            self.all_food_data[food_dict["Name"]] = food_dict

        # change directory back to home
        os.chdir("..\\..")

    # loop through food eaten today json file and calculate total nutrition facts eaten today
    def calculate_nutrition_facts(self):
        # open food_today.json
        file = open("food_today.json", 'r')

        # load json file
        food_json = json.load(file)

        # close file
        file.close()

        # loop through food_json input dict
        for food_name, food_amount in food_json.items():
            # get serving size from all_food_data dict
            serving_size = self.all_food_data[food_name]["Serving Size"]

            # loop through "Food Data" dict in all_food_data dict at food_name
            for nutrit_fact_name, nutrit_fact_amount in self.all_food_data[food_name]["Food Data"].items():
                # update all_food_content dict at specified nutrition fact
                self.all_food_content[nutrit_fact_name] += (food_amount / serving_size) * nutrit_fact_amount

    # print info to console on total Nutrition Facts
    def print_data(self):
        # open output data file
        file = open("Nutrition_For_Today.txt", 'w')

        # start writing data to file
        file.write("Total Nutrition Facts Consumed Today\n")

        # loop through all_food_content dictionary and print data
        for nutrition_fact_name, nutrition_fact_amount in self.all_food_content.items():
            # write data to text file
            file.write(f"{nutrition_fact_name}: {round(nutrition_fact_amount,2)} {self.all_food_content_units[nutrition_fact_name]}\n")

        # close output file
        file.close()

# End of Calorie Counter Class
#==================================================================================================================================

# Driver
stuff = CalorieCounter()
stuff.fill_lists()
stuff.fill_dicts()
stuff.calculate_nutrition_facts()
stuff.print_data()