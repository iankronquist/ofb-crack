import os
import random
from operator import xor


BLOCK_SIZE = 256
KEY_SIZE = 1024
 
def hex_print(ba):
    """Prints the colon separated hexidecimal values of each byte in a
    bytearray"""
    print ":".join("{:02x}".format(c) for c in ba)


def PRF(text, key):
    # FIXME: This is *definitely* a secure PRF
    random.seed(str(text) + str(key))
    return bytearray([random.randint(0, 255) for _ in xrange(len(text))])


def ofb_block(inbound, text, key):
    """A single OFB mode sub-section.
    bytearray -> bytearray -> bytearray -> bytearray"""
    stream = block_cipher(inbound, key)
    outbound = XOR(text, stream)
    return outbound

       
def block_cipher(text, key):
    """A four round block cipher, straight out of the book"""
    # Assert that the text is of an even length
    assert len(text) & 1 == 0
    half = len(text)/2
    left = text[:half]
    right = text[half:]
    for block_round in range(1):
        tmp = right
        right = PRF(XOR(left, right), key)
        left = tmp
    return left + right
    

def ofb_encrypt(plain, key):
    plain = pad(plain)
    # Initialize prev_block with IV
    prev_block = bytearray(os.urandom(BLOCK_SIZE))
    yield prev_block
    for block in blocks(plain, BLOCK_SIZE):
        yield ofb_block(prev_block, block, key)
        prev_block = block


def ofb_decrypt(cipher, key):
    gen_blocks = blocks(cipher, BLOCK_SIZE)
    # The first block is the IV, don't decrypt it.
    prev_block = next(gen_blocks)
    for block in gen_blocks:
        yield ofb_block(prev_block, block, key)
        prev_block = block
        

def pad(block):
    pad_zeros = (BLOCK_SIZE - len(block)) - 1
    if pad_zeros == 0:
        pad_zeros = BLOCK_SIZE - 1
    block += '\0' * pad_zeros
    block += chr(pad_zeros)
    assert len(block) % BLOCK_SIZE == 0
    return block


def strip(block):
    padding = block[-1]
    # Don't check the padding - that can lead to a padding oracle attack
    # assert all(map(lambda x: x == 0, block[len(block)-padding:-1]))
    return block[:(len(block) - padding - 1)]


def XOR(a, b):
    """xors two bytearrays of equal length"""
    return bytearray(map(xor, a, b))


def blocks(ba, block_len):
    """Yield successive n-sized chunks from the bytearray."""
    for i in xrange(0, len(ba), block_len):
        yield ba[i:i+block_len]
