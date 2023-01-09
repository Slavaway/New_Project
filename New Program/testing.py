import unittest
import Main_Func



# Тестирую нахождение площади

class TestFind_S(unittest.TestCase):
    def test_Square(self):
        self.assertEqual(Main_Func.Square(3, 6), 18)


# Тестирую нахождение периметра

class TestFind_P(unittest.TestCase):

    def test_Perimeter(self):
       self.assertEqual(Main_Func.Perimeter(3, 6), 18)




if __name__ == "__main__":
    unittest.main()
