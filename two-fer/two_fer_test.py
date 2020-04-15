import unittest

from two_fer import two_fer

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0


class TwoFerTest(unittest.TestCase):
    # good case
    def test_no_name_given(self):
        self.assertEqual(two_fer(), "One for you, one for me.")

    def test_a_name_given(self):
        self.assertEqual(two_fer("Alice"), "One for Alice, one for me.")

    def test_another_name_given(self):
        self.assertEqual(two_fer("Bob"), "One for Bob, one for me.")
    
    def test_bad_case(self):
        self.assertEqual(two_fer(['Bob']), None)
    
    def test_bad_case_1(self):
        self.assertEqual(two_fer(1), None)

    def test_edge_case(self):
        self.assertEqual(two_fer(""), "One for you, one for me.")

if __name__ == "__main__":
    unittest.main()
