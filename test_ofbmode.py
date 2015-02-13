import unittest
import mock
import ofbmode


class TestOfbMode(unittest.TestCase):
    def test_xor(self):
        a = 'abcd'
        zeros = '\0' * 4
        ones = '\xff' * 4
        self.assertEqual(ofbmode.XOR(a, a), zeros)
        self.assertEqual(ofbmode.XOR(a, zeros), a)
        #self.assertEqual(XOR(a, ones), a_inverse)
