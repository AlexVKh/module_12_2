import module_12_2 as m
import unittest

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.a = m.Runner('Усэйн', 10)
        self.b = m.Runner('Андрей', 9)
        self.c = m.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i in range(len(cls.all_results)):
            print(cls.all_results[i])

    def test_d1(self):
        t = m.Tournament(90, self.a, self.c)
        self.all_results.append(t.start())
        self.assertTrue(self.all_results[-1][max(self.all_results[-1].keys())] == 'Ник')

    def test_d2(self):
        t = m.Tournament(90, self.c, self.b)
        self.all_results.append(t.start())
        self.assertTrue(self.all_results[-1][max(self.all_results[-1].keys())] == 'Ник')

    def test_d3(self):
        t = m.Tournament(90, self.a, self.b, self.c)
        self.all_results.append(t.start())
        self.assertTrue(self.all_results[-1][max(self.all_results[-1].keys())] == 'Ник')

if __name__ == '__main__':
    unittest.main()

