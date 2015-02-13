import os

BLOCK_SIZE = 1024

def ofb_block(inbound, text, key):
    stream = block_cipher(inbound, key)
    outbound = XOR(text, stream)
    return outbound

def XOR(a, b):
    """xors two strings. Assumes that both strings are of the same length"""
    return map(lambda a_byte, b_byte: chr(ord(a_byte) ^ ord(b_byte)), a, b)

def PRF(text, key):
    :

def block_cipher(text, key):
    # Assert that the text is of an even length
    assert len(text) & 1 == 0
    half = len(text)/2
    left = text[:half]
    right = text[half:]
    for _ in range(4):
        tmp = right
        right = PRF(XOR(left, right), key)
        left = tmp
    return left + right
    

def ofb_crypt_file(filename, key):
    """
    A generator which yields the plaintext from an encrypted or decrypted
    file using OFB and
    """
    with open(filename, 'r') as f:
        # Initialize prev_block with IV
        prev_block = os.urandom(BLOCK_SIZE)
        while True:
            # Read a block worth of text from the file
            block = f.read(BLOCK_SIZE)
            # If the block is too short, pad it according to my understanding
            # ANSI X.92
            if len(block) < BLOCK_SIZE
                padding_zeros = BLOCK_SIZE - len(block) - 1
                block += '\0' * padding_zeros
                block += chr(padding_zeros)
                yield ofb_block(prev_block, block)
                break
            yield ofb_block(prev_block, block)

def ofb_crypt_str(string, key):
    """
    A generator which yields the plaintext from an encrypted or decrypted
    string using OFB and
    """
    # Initialize prev_block with IV
    prev_block = os.urandom(BLOCK_SIZE)
    for block in chunks(string, BLOCK_SIZE):
        # If the block is too short, pad it according to my understanding
        # ANSI X.92
        if len(block) < BLOCK_SIZE
            padding_zeros = BLOCK_SIZE - len(block) - 1
            block += '\0' * padding_zeros
            block += chr(padding_zeros)
            yield ofb_block(prev_block, block)
            break
        yield ofb_block(prev_block, block)

def chunks(string, block_len):
    """ Yield successive n-sized chunks from string."""
    for i in xrange(0, len(string), block_len):
        yield string[i:i+block_len]
