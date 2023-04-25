import unittest
import MineCell

class TestMinesweeper(unittest.TestCase):
        def test_cell(self):
            M = MineCell.Cell(True)
            self.assertTrue(M.is_bomb())
            self.assertEqual(M.appears(), '+')
            M.toggle_flag()
            self.assertEqual(M.appears(), 'F')
