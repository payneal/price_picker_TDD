# Price code

class Price:
    def __init__(self):
        self.product_info = None
        self.price_point = None
        self.original_info = None

    def price_optimisation(self, product_info, price_points):
        self.original_info = product_info
        self.price_points = price_points
        self.product_info = product_info
        return self.execute_optimization()

    def execute_optimization(self):
        self.make_sure_price_rounded_to_two_decimals()
        self.get_min_to_max_range()
        self.second_decimal_must_be_in_price_point()
        self.price_close_to_original()
        self.convert_back_to_float(["maximum" , "minimum"])
        return self.product_info
     
    def make_sure_price_rounded_to_two_decimals(self):
        self.round_to_2_decimal_places('original', 2)
        self.round_to_2_decimal_places('minimum', 2)
        self.round_to_2_decimal_places('maximum', 2)

    def round_to_2_decimal_places(self, key_name, decimal_position):
        self.product_info[key_name] =\
            "%.2f" % round(self.product_info[key_name],decimal_position)

    def get_min_to_max_range(self):
        max_range, min_range = self.max_and_min_values()
        self.product_info['range_of_answers'] =\
            range(int(min_range), int(max_range))

    def max_and_min_values(self):
        return  self.decimal_to_string_no_period('maximum'),\
            self.decimal_to_string_no_period('minimum')

    def convert_back_to_float(self,list_of_converts):
        for x in list_of_converts:
            self.product_info[x] = float(self.product_info[x]) 

    def second_decimal_must_be_in_price_point(self):
        hold = []
        for i, possible_option in enumerate(self.product_info['range_of_answers']):
            last_number = int(str(possible_option)[-1:][0])
            hold = self.is_vaild_via_price_points(hold, last_number, possible_option)
        self.product_info['range_of_answers'] = hold

    def is_vaild_via_price_points(self, hold, last_number, possible_option):
        for x in self.price_points:
            if x == last_number:
                hold.append(possible_option)
        return hold

    def price_close_to_original(self):

        if len(self.product_info['range_of_answers']) == 0:
            self.product_info['new_price'] = "No price point withmin / max range";
        else:
            self.calculate_closest()
        del self.product_info['range_of_answers']
    
    def calculate_closest(self): 
        og = int(self.decimal_to_string_no_period('original'))
        best_option = str(
            min(self.product_info['range_of_answers'], key=lambda x:abs(x - og)))
        self.product_info['new_price'] = float(best_option[:-2] + "." + best_option[-2:])
        
    def decimal_to_string_no_period(self, name):
        return (str(self.product_info[name]).replace(".", ""))

