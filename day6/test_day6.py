import unittest

from day6.day6 import Memory


class MyTestCase(unittest.TestCase):
    def test_1(self):
        m = Memory([0, 2, 7, 0])
        self.assertEqual(m.memory, [0, 2, 7, 0])

    def test_2(self):
        m = Memory([0, 2, 7, 0])
        i = m.get_max_blocks_index()
        self.assertEqual(i, 2)

    def test_3(self):
        m = Memory([0, 2, 7, 0])
        m.save_state()
        self.assertEqual(m.memory, m.prev_states[0])

    def test_4(self):
        m = Memory([0, 2, 7, 0])
        m.re_dist()
        self.assertEqual(m.memory, [2, 4, 1, 2])

    def test_5(self):
        m = Memory([0, 2, 7, 0])
        m.save_state()
        m.re_dist()
        m.save_state()
        m.re_dist()
        m.save_state()
        self.assertEqual(m.memory, [3, 1, 2, 3])
        self.assertEqual(m.prev_states[0], [0, 2, 7, 0])
        self.assertEqual(m.prev_states[1], [2, 4, 1, 2])
        self.assertEqual(m.prev_states[2], [3, 1, 2, 3])

    def test_6(self):
        m = Memory([0, 2, 7, 0])
        self.assertEqual(m.re_alloc(), 5)

    def test_7(self):
        m = Memory([0, 2, 7, 0])
        m.re_alloc()
        self.assertEqual(m.loop_size, 4)


if __name__ == '__main__':
    unittest.main()
