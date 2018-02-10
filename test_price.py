# test cases

import unittest
from price import Price

class Test_Price_Case(unittest.TestCase):

    def setUp(self):
        self.price = Price();

    def tearDown(self):
        pass

    def test_the_the_price_is_rounded_down_two_decimal_points(self):

        product_a = {
            "original": 2.91,
            "minimum": 2.89,
            "maximum": 2.97} 
        new_product_a  = self.price.price_optimisation(product_a, [2, 3, 7])
        self.assertEqual( new_product_a["new_price"], 2.92);
        
    def test_new_price_inbetween_min_and_max(self):

        product_a = {
            "original": 2.91,
            "minimum": 2.89,
            "maximum": 2.97} 
        new_product_a  = self.price.price_optimisation(product_a, [2, 3, 7])
        self.assertGreaterEqual( new_product_a["new_price"], product_a["minimum"]);
        self.assertLessEqual( new_product_a["new_price"], product_a["maximum"]);
    
    
    def test_new_price_second_decimal_must_be_in_price_points(self):
        product_a = {
            "original": 2.91,
            "minimum": 2.89,
            "maximum": 2.97} 
        new_product_a  = self.price.price_optimisation(product_a, [2, 3, 7])
            
        # get second element in a string
        new_price = str(new_product_a['new_price'])
        new_price = int(new_price[-1:])
        if new_price in [2, 3, 7]:
            self.assertEqual(True, True)
        else:
            self.assertEqual(False, True)

    def test_new_price_is_as_close_as_possible_to_original_price(self):
        product_a = {
            "original": 2.91,
            "minimum": 2.89,
            "maximum": 2.97} 
        new_product_a  = self.price.price_optimisation(product_a, [2, 3, 7])
        self.assertEqual( new_product_a["new_price"], 2.92);
    
    
    def test_2_the_the_price_is_rounded_down_two_decimal_points(self):
   
        product_b = {
            "original": 3.64,
            "minimum": 3.69,
            "maximum": 3.73} 
        new_product_b  = self.price.price_optimisation(product_b, [2, 3, 7])
        self.assertEqual( new_product_b["new_price"], 3.72);
  
    def test_3_the_the_price_is_rounded_down_two_decimal_points(self):
    
        product_c = {
            "original": 3.65,
            "minimum": 3.65,
            "maximum": 3.66} 
        new_product_c  = self.price.price_optimisation(
            product_c, [2, 3, 7])
        self.assertEqual(
            new_product_c["new_price"], "No price point withmin / max range");
  
if __name__ == '__main__':
    unittest.main()
