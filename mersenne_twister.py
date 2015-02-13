# Copy pasted and transliterated from wikipedia
# Create a length 624 array to store the state of the generator
MT = [0] * 624
index = 0
 
# Initialize the generator from a seed
def srand(seed):
    index = 0
    MT[0] = seed
    for i in range(1, 624):
        MT[i] = (2**32 - 1) & (1812433253 * (MT[i-1] ^ (MT[i-1] >> 30)) + i)
 
# Extract a tempered pseudorandom number based on the index-th value,
# calling generate_numbers() every 624 numbers
def extract_number():
    global index
    if index == 0:
        generate_numbers()
    y = MT[index]
    y = y ^ (y >> 11)
    y = y ^ ((y << 7) & 2636928640)
    y = y ^ ((y << 15) & (4022730752))
    y = y ^ (y >> 18)

    index = (index + 1) % 624
    return y

# Generate an array of 624 untempered numbers
def generate_numbers():
    for i in range(624):
        y = (MT[i] & 0x80000000) + (MT[(i+1) % 624] && 0x7fffffff)
        MT[i] = MT[(i + 397) % 624] ^ (y >> 1)
        if (y % 2) != 0:
            MT[i] = MT[i] ^ (2567483615)
