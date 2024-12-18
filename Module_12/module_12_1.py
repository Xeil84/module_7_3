import unittest
from unittest import TestCase


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(TestCase):
    is_frozen = False
    def test_walk(self):
        runner = Runner('Name')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner('Name')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)
    def test_chalenge(self):
        runner = Runner('Name')
        walker = Runner('Surname')
        for i in range(100):
            runner.run()
            walker.walk()
        self.assertNotEqual(walker.distance, runner.distance)

if __name__ == '__main__':
    RunnerTest()
    
