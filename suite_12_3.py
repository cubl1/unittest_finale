import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self, times=1):
        for i in range(times):
            self.distance += 10
        return self.distance

    def walk(self, times=1):
        for i in range(times):
            self.distance += 5
        return self.distance

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        runner = Runner("h")
        self.assertEqual(runner.walk(10), 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        runner = Runner("i")
        self.assertEqual(runner.run(10), 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        runner1 = Runner("j")
        runner2 = Runner("k")
        runner1.run(10)
        runner2.walk(10)
        self.assertNotEqual(runner1.distance, runner2.distance)

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
    @classmethod
    def setUpClass(cls):
        cls.all_results = []
    def setUp(self):
        self.r1 = Runner("Усэйн", 10)
        self.r2 = Runner("Андрей", 9)
        self.r3 = Runner("Ник", 3)
    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_t1(self):
        t1 = Tournament(90, [self.r1, self.r3])
        self.assertTrue(t1[2]== self.r3)
        self.all_results.append(t1)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_t2(self):
        t2 = Tournament(90, [self.r2, self.r3])
        self.assertTrue(t2[2] == self.r3)
        self.all_results.append(t2)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_t3(self):
        t3 = Tournament(90, [self.r1, self.r2, self.r3])
        self.assertTrue(t3[3] == self.r3)
        self.all_results.append(t3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results:
            print(i)

if __name__ == "__main__":
    ts = unittest.TestSuite
    ts.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
    ts.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

    ttr = unittest.TextTestRunner(verbosity=2)
    ttr.run(ts)
