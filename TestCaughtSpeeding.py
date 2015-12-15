import unittest

import StudentTest

class KnownValues(unittest.TestCase):
    known_values = ( (60, 'n', 0),
                     (61, 'n', 500),
                     (65, 'n', 500),
                     (65, 'y', 0),
                     (80, 'n', 500),
                     (81, 'n', 1000),
                     (85, 'n', 1000),
                     (85, 'y', 500),
                     (91, 'n', 1000),
                     (55, 'y', 0)
                     )
    def test_speeding_known_values(self):
        """ test_speeding_known_values """
        for i in self.known_values:
            result = StudentTest.getTicket(i[0], i[1])
            self.assertEqual(i[2], result)

if __name__ == '__main__':
    unittest.main()

