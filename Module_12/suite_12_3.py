import unittest
from Module_12 import module_12_1
from Module_12 import tests_12_3

test_no1 = unittest.TestSuite()
test_no1.addTests(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
test_no1.addTests(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_no1)

