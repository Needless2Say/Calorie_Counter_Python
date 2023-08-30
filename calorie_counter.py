from collections import defaultdict

'''Calorie Counter Class'''
class CalorieCounter:
    # All Nutrition Fact Labels

    all_food_content =  ["Calories","Total Fat","Saturated Fat","Trans Fat","Polyunsaturated Fat","Monounsaturated Fat","Cholesterol","Sodium","Potassium",
    "Total Carbohydrates","Dietary Fiber","Soluble Fiber","Dietary Sugars","Total Sugars","Added Sugars","Erythritol","Protein"]

    # Base Numbers for keeping track of total amount consumed of each nutrition fact
    all_food_content_amount = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    # Units for all Nutrition Facts
    all_food_content_units = ["calories", "grams", "grams", "grams", "grams", "grams", "milligrams", "milligrams",
    "milligrams", "grams", "grams", "grams", "grams", "grams", "grams", "grams", "grams"]

#==================================================================================================================================
    # Variables for Storing Info

    ''' Dictionaries for storing Nutrition Facts

    Note:
    The nutirition facts are all based on the ones specified in the list all_food_content.
    Any missing values will be treated as 0 as shown in the info.txt file

    Dictionary food_info_amount
    Keeps track of the name of the food as the key
    Stores the amount for each Nutrition Fact in a list
    dict(string, list[double])

    Dictionary food_serving_size
    Keeps track of the name of the food as the key
    Stores the serving size of the food
    '''
    food_info_amount = defaultdict(list)
    food_serving_size = defaultdict(list)

    ''' Dictionary for food amount consumed from user input file

    Keeps track of the food and the serving size of each food consumed
    '''
    food_info_input = defaultdict(list)


    ''' Dictionary for total amount consumed

    Keeps track of the name of the food as the key
    Stores the total amount of units consumed for each Nutrition Fact    
    '''
    food_info_calculated = defaultdict(list)

#==================================================================================================================================
    # Functions

    ''' Function for getting info from info.txt -> get_info()

    REQUIRES: info.txt has food info and values for all nutrition labels
    MODIFIES: NA
    EFFECTS: fills in dictionaries food_info_amount and food_serving_size
    '''
    def get_info(self):
        file = open('info.txt', 'r')
        count = 0
        list_temp = []
        cur_food = ""

        for line in file:
            if line == "\n" or line == "END":
                count = 0
                self.food_info_amount[cur_food] = [x for x in list_temp]
                list_temp.clear()
                continue

            words = line.split()
            if count == 0:
                cur_food = words[0]
                self.food_serving_size[cur_food] = float(words[1])
            else:
                list_temp.append(float(words[1]))
            count += 1

        file.close()

#======================================================================== End of function get_info()

    ''' Function for checking serving size -> check_serving_size()

    REQUIRES: food_info_amount and food_serving_size are filled in with info
    MODIFIES: food_serving_size
    EFFECTS: changes numbers for each nutrition fact for each food by dividing
    the values by the serving size, and then dividing the serving size by itself
    to get 1
    '''
    def check_serving_size(self):
        for food, serving_size in self.food_serving_size.items():
            if(serving_size != 1):
                # divide amount by serving size so serving size is equal to 1 for easier calculations
                self.food_info_amount[food] = [(num/serving_size) for num in self.food_info_amount[food]]

                # divide serving size by itself to set it to 1
                self.food_serving_size[food] = self.food_serving_size[food]/self.food_serving_size[food]

#======================================================================== End of function check_serving_size()

    ''' Function for getting info on total food eaten by user -> input_info_manual()

    REQUIRES: input.txt has info in proper format
    MODIFIES: food_info_input
    EFFECTS: stores the food name and serving size specified in file
    '''
    def input_info_manual(self):
        file = open('input.txt', 'r')
        for line in file:
            if line == "END":
                break

            # split line into food name and serving size eaten
            info = line.split()

            # store name of food as key and serving size as value associated with key
            self.food_info_input[info[0]] = float(info[1])

#======================================================================== End of function input_info_manual()

    ''' Function for calculating total amount consumed -> calculate_total_food_content()

    REQUIRES: food_info_amount, food_serving_size, and food_info_input contain proper info
    MODIFIES: food_info_calculated
    EFFECTS: calculates total amount of each nutrition lablel consumed and
    stores it in food_info_calculated dictionary
    '''
    def food_info_calculated(self):
        for food, serving_size in self.food_info_input.items():
            food_info = self.food_info_amount[food]
            for uni_index in range(len(self.all_food_content_amount)):
                self.all_food_content_amount[uni_index] += food_info[uni_index]*serving_size

#======================================================================== End of function food_info_calculated()

    ''' Function for storing total info in a file -> input_info_textfile()
    
    REQUIRES: food_info_calculated contains info stored properly
    MODIFIES: NA
    EFFECTS: writes all nutrition facts in proper format to a text file
    '''
    def input_info_textfile(self):
        file = open("Nutrition_For_Today.txt", 'w')
        for uni_index in range(17):
            file.write("{}: {} {}\n".format(self.all_food_content[uni_index],round(self.all_food_content_amount[uni_index],2),self.all_food_content_units[uni_index]))
        file.close()

#======================================================================== End of function input_info_textfile()

# End of Calorie Counter Class
#==================================================================================================================================

# Main Function for calculating info
stuff = CalorieCounter()
stuff.get_info()
stuff.check_serving_size()
stuff.input_info_manual()
stuff.food_info_calculated()
stuff.input_info_textfile()