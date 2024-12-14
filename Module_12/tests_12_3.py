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

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        walker = Runner('Name')
        for i in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner = Runner('Name')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_chalenge(self):
        runner = Runner('Name')
        walker = Runner('Surname')
        for i in range(100):
            runner.run()
            walker.walk()
        self.assertNotEqual(walker.distance, runner.distance)

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class TournamentTest(unittest.TestCase):
    is_frozen = True
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_usain_and_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        result = tournament.start()
        result_str = {k: str(v) for k, v in result.items()}
        self.__class__.all_results.update({1: result_str})
        self.assertTrue(result[max(result.keys())] == "Ник")

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        result = tournament.start()
        result_str = {k: str(v) for k, v in result.items()}
        self.__class__.all_results.update({2: result_str})
        self.assertTrue(result[max(result.keys())] == "Ник")

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_usain_andrey_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        result = tournament.start()
        result_str = {k: str(v) for k, v in result.items()}
        self.__class__.all_results.update({3: result_str})
        self.assertTrue(result[max(result.keys())] == "Ник")

if __name__ == '__main__':
    RunnerTest()
    TournamentTest()

