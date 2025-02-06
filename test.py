import unittest;
from main import fizzbuzz;

# def test_fizzbuzz():
#     assert fizzbuzz(1) == "1"
#     assert fizzbuzz(3) == "Fizz"
#     assert fizzbuzz(4) == "4"
#     assert fizzbuzz(5) == "Buzz"
#     assert fizzbuzz(15) == "FizzBuzz"

class TestFizzBuzz(unittest.TestCase): # definition d'une classe de test

    def test_multiple_de_3(self): # definition d'une methode de test
        self.assertEqual(fizzbuzz(3), "Fizz") # Vérifie que la sortie attendue correspond à la sortie réelle : self.assertEqual(actual, expected)
        self.assertEqual(fizzbuzz(6), "Fizz")

    def test_multiple_de_5(self):
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(10), "Buzz")

    def test_multiple_de_3_et_5(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
        self.assertEqual(fizzbuzz(30), "FizzBuzz")

    def test_pas_multiple_de_3_ni_5(self):
        self.assertEqual(fizzbuzz(1), "1")
        self.assertEqual(fizzbuzz(7), "999")

if __name__ == '__main__':
    unittest.main()
