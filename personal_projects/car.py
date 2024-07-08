import unittest

def square(num):
  return num * num
# Write test methods to check different scenarios 
# (e.g., valid input, invalid input) and verify expected behavior.

class TestSquare(unittest.TestCase):
    
  def test_square_operations(self):
    answer = square(4)
    self.assertEqual(answer,16)
    
  def test_valid_number(self):
    num = input("Enter a number to be squared: ")
    
    #Check if input is valid number
    self.assertEqual(num.isnumeric(),True)
      
    
    
if __name__ == "__main__":
  unittest.main()
  
