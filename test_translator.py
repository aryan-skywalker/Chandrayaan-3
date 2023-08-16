import unittest
from translator import translator

class TestChandrayaan_3(unittest.TestCase):
    def setUp(self):
        # create a Chandrayaan-3 object with initial position (0, 0, 0) and direction N
        self.translator = translator(0, 0, 0, "N")

    def tearDown(self):
        # delete the Chandrayaan-3 object
        del self.translator
    
    # Define a test method to check the initialization of the Chandrayaan-3
    def test_init(self):
        # Assert that the attributes are correctly assigned
        self.assertEqual(self.translator.x, 0)
        self.assertEqual(self.translator.y, 0)
        self.assertEqual(self.translator.z, 0)
        self.assertEqual(self.translator.direction, "N")
    
    # move the Chandrayaan-3 forward
    def test_execute_forward(self):
        t = translator(0, 0, 0, "N")
        t.execute(["f"])
        self.assertEqual(t.y, 1)

    # move the Chandrayaan-3 backward
    def test_execute_backward(self):
        t = translator(0, 0, 0, "N")
        t.execute(["b"])
        self.assertEqual(t.y, -1)
           
    # Turn the Chandrayaan-3 left
    def test_execute_turn_left(self):
        # Turn the Chandrayaan-3 if initial direction in North
        t = translator(0, 0, 0, "N")
        t.execute(["l"])
        self.assertEqual(t.direction, "W")
        # Turn the Chandrayaan-3 if initial direction in South
        t = translator(0, 0, 0, "S")
        t.execute(["l"])
        self.assertEqual(t.direction, "E")
        # Turn the Chandrayaan-3 if initial direction in East
        t = translator(0, 0, 0, "E")
        t.execute(["l"])
        self.assertEqual(t.direction, "N")
        # Turn the Chandrayaan-3 if initial direction in West
        t = translator(0, 0, 0, "W")
        t.execute(["l"])
        self.assertEqual(t.direction, "S")

    # Turn the Chandrayaan-3 right
    def test_execute_turn_right(self):
        # Turn the Chandrayaan-3 if initial direction in North
        t = translator(0, 0, 0, "N")
        t.execute(["r"])
        self.assertEqual(t.direction, "E")
        # Turn the Chandrayaan-3 if initial direction in South
        t = translator(0, 0, 0, "S")
        t.execute(["r"])
        self.assertEqual(t.direction, "W")
        # Turn the Chandrayaan-3 if initial direction in East
        t = translator(0, 0, 0, "E")
        t.execute(["r"])
        self.assertEqual(t.direction, "S")
        # Turn the Chandrayaan-3 if initial direction in West
        t = translator(0, 0, 0, "W")
        t.execute(["r"])
        self.assertEqual(t.direction, "N")
        
    def test_tilt_up(self):
        # Tilt the Chandrayaan-3 up
        self.translator.tilt("u")
        # Assert that the direction is updated to "Up"
        self.assertEqual(self.translator.direction, "Up")
        
    def test_tilt_down(self):
        # Tilt the Chandrayaan-3 down
        self.translator.tilt("d")
        # Assert that the direction is updated to "Down"
        self.assertEqual(self.translator.direction, "Down")
    
    # Define a test method to check the move method of the Chandrayaan-3
    def test_move_multiple(self):
        # Move the Chandrayaan-3 forward by one unit
        self.translator.move("f")
        # Assert that the position is updated to (0, 1, 0)
        self.assertEqual(self.translator.x, 0)
        self.assertEqual(self.translator.y, 1)
        self.assertEqual(self.translator.z, 0)
    
        # Move the Chandrayaan-3 backward by two units
        self.translator.move("b")
        self.translator.move("b")
        # Assert that the position is updated to (0, -1, 0)
        self.assertEqual(self.translator.x, 0)
        self.assertEqual(self.translator.y, -1)
        self.assertEqual(self.translator.z, 0)
    
    # Taking input for commands Character array of commands (f, b, l, r, u, d)
    def test_execute_multiple_commands(self):
        t = translator(0, 0, 0, "N")
        t.execute(["f", "r", "u", "b", "l"])
        self.assertEqual(t.x, 0)
        self.assertEqual(t.y, 1)
        self.assertEqual(t.z, -1)
        self.assertEqual(t.direction, "N")

if __name__ == "__main__": 
    unittest.main()