import os
import unittest
import operator
import ofbmode


class TestOfbMode(unittest.TestCase):

    def test_xor(self):
        a = bytearray('abcd')
        zeros = bytearray('\0' * 4)
        ones = bytearray('\xff' * 4)
        self.assertEqual(ofbmode.XOR(a, a), zeros)
        self.assertEqual(ofbmode.XOR(a, zeros), a)

    def test_strip(self):
        s = bytearray('test\x00\x00\x00\x03')
        self.assertEqual(bytearray('test'), ofbmode.strip(s))

    def test_pad(self):
        t = bytearray('test')
        expected = bytearray('test' + '\x00' * 251 + chr(251))
        self.assertEqual(expected, ofbmode.pad(t))
    
    def test_ofb_crypt(self):
        key = bytearray(os.urandom(ofbmode.KEY_SIZE))
        plaintext = bytearray('hello world')
        ciphertext = ofbmode.ofb_encrypt(plaintext, key)
        ciphertext_str = reduce(operator.add, ciphertext)
        dec_plaintext = ofbmode.ofb_decrypt(ciphertext_str, key)
        dec_plaintext_str = reduce(operator.add, dec_plaintext)
        self.assertNotEqual(ciphertext_str, dec_plaintext_str)
        self.assertEqual(plaintext, dec_plaintext_str)

    def test_blocks(self):
        a = bytearray('12345')
        self.assertEqual(map(lambda x: x, ofbmode.blocks(a, 2)),
            map(bytearray, ['12', '34', '5']))
