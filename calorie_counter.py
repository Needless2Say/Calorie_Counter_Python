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
        
        # loop through dictionary
        for label, units in file:
            # add label to all_food_content list
            self.all_food_content[label] = 0
            
            # add units to all_food_content_units
            self.all_food_content_units[label] = units
        
        # close file
        file.close()
        
    # fill dictionary all_food_data from food in folder to_input/food
    def fill_dicts(self):
        # open directory where all foods are stored
        os.chdir("something on main desktop")
        
        # loop through all food files in directory
        for filename in os.listdir():
            # open file
            file = open(filename, 'r')
            
            # read json file
            food_dict = json.load(filename)
            
            # get serving size from food_dict
            serving_size = food_dict["Serving Size"]
            
            # loop through "Food Data" dictionary in food dictionary and adjust nutrition facts by dividing everything by serving size
            # then set serving size to 1
            # (this helps with making total nutrition facts calculations easier)
            for stuff in food_dict["Food Data"]:
                # adjust nutrition fact by dividing by serving size
                food_dict["Food Data"][stuff] = food_dict["Food Data"][stuff] / serving_size
                
            # set serving size to 1 in food_dict after adjustments to nutrtion facts in "Food Data" dictionary
            food_dict["Serving Size"] = 1
            
            # add "Food Data" dictionary to all_food_data dictionary
            # key = food name, value = food data dictionary
            self.all_food_data[food_dict["Name"]] = food_dict["Food Data"]
            
            # close file
            file.close() 

    # loop through food eaten today json file and calculate total nutrition facts eaten today
    def calculate_nutrition_facts(self):
        # open food_today.json
        file = open("food_today.json", 'r')
          
        # loop through dictionary and calculate nutrition facts and update all_food_content dictionary
        for food_name, food_amount in file:
            # loop through food nutrition facts in food_name dictionary
            for nutrition_fact_name, nutrition_fact_amount in self.all_food_data[food_name]:
                # multipy food_amount to nutrition_fact_amount and add it to all_food_content at nutrition_fact_name
                self.all_food_content[nutrition_fact_name] += nutrition_fact_amount * food_amount
        
        # close file
        file.close()

#======================================================================== End of function food_info_calculated()



#======================================================================== End of function input_info_textfile()

# End of Calorie Counter Class
#==================================================================================================================================

# Driver
stuff = CalorieCounter()
stuff.get_info()
stuff.check_serving_size()
stuff.input_info_manual()
stuff.food_info_calculated()
stuff.input_info_textfile()