# implement AES like symmetric encryption
# limited to encrypting capital alpha characters only

# subBytes function - used sbox to substitute bytes in matrix
def subBytes(matrix, sbox):
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if (matrix[r][c] != ' '):
                matrix[r][c] = sbox[matrix[r][c]]

def shiftRows(matrix):
    # shift each row to the left starting with 2nd row and incrementing
    # shift for each additional row
    for r in range(1, len(matrix)):
        matrix[r] = matrix[r][r:len(matrix[r])] + matrix[r][0:r]
        # start in row r
        # takes the columns and shifts them up to the last col, creates new array with item from position of row length to the end
        # the first column is appended to the end
        # 'o', 'w', 'o', 'r'
        # 'w', 'o', 'r', 'o'
        # column 1, shifted by 1
        # column 2, shifted by 2
        # ...
    return matrix

def mixColumns(matrix):
    # the steps to perform mixColumns has not been implemented
    # this step requires converting bytes into polynomials, performing
    # matrix multiplication and then converting the result back to bytes
    return matrix

def addRoundKey(roundkey, matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            # convert character to binary for data and key
            b1 = getBinary(matrix[r][c]) # gets the binary value of the character
            b2 = getBinary(roundkey[r][c]) # gets the binary value of the character
            # xor data with key
            matrix[r][c] = xor(b1, b2) # XORs the binary values
            # convert binary back to integer
            matrix[r][c] = int(matrix[r][c], 2) # Converts to integer the location of the matrix from base 2 (binary)
            # convert integer back to character
            matrix[r][c] = chr(matrix[r][c]) # Converts the location of the matrix from int to character


def xor(b1, b2):
    val = ''
    for i in range(len(b1)):
        if b1[i] == '0' and b2[i] == '0':
            val = val + '0'
        elif b1[i] == '0' and b2[i] == '1':
            val = val + '1'
        elif b1[i] == '1' and b2[i] == '0':
            val = val + '1'
        else:
            val = val + '0'
    return val

def makeSbox(sbox):
    # substitution box simply performs a shift 1
    # for i in range(65, 90):
    #     sbox[chr(i)] = chr(i+1)
    # sbox['Z'] = 'A'
    for i in range(0, 256):
        sbox[chr(i)] = chr(i+1)
    sbox['ÿ'] = chr(0)

def getBinary(letter):
    binary = ''
    val = bin(ord(letter)) # converts char to int then to binary (adds '0b' to the front)
    val = val.removeprefix('0b') # removes the UTF-8 prefix from the value
    for i in range(8-len(val)):
        val = '0' + val
    return val

def createMatrix(text, numcols):
    matrix = []
    row = []
    col = 0  # counter for number of elements in row
    i = 0    # holds the index of the character in text
    for i in range(len(text)):
        row.append(text[i]) # adds a letter to the current row
        col += 1
        # if full row built - add row to matrix and reset row
        if (col == numcols or i == (len(text) - 1)):
            matrix.append(row) # adds the created row to the matrix
            row = []
            col = 0

    # if last row was incomplete, pad with spaces
    lastRowLen = len(matrix[-1]) # Grabs the last row of the matrix and gets its length
    pad = numcols - lastRowLen # Compares the number of columns and how long a row is with characters
    for i in range(pad): # If padding is required, "pad" will be greater than 0
        matrix[-1].append(' ') # Pads the last row with space

    # pad with rows to create numcols X numcols matrix
    morerows = numcols - len(matrix) # Checks if more rows must be added

    if (morerows > 0):
        # create empty row
        row = []
        for i in range(numcols):
            row.append(' ') # fills the row with spaces
        for i in range(morerows):
            matrix.append(row) # adds the remaining rows (if applicable) of spaces
    return matrix

def main():
    sbox = {}
    makeSbox(sbox)
    ptext = 'HELLOWORLD'
    # create one block of plaintext as a 4X4 matrix - may need padding
    matrix = createMatrix(ptext, 4)
    print("Plaintext in matrix format:")
    print(matrix)
    for i in range(2):
        print("--------")
        subBytes(matrix, sbox)
        print("Matrix after subBytes:")
        print(matrix)
        shiftRows(matrix)
        print("Matrix after shiftRows:")
        print(matrix)
        # #mixColumns(matrix) - not implemented
        # # each round would use a different round key which is generated using
        # # a key schedule - each round key is 128 bits - 16 bytes
        # # this implementation uses a hardcoded value for the one round key and
        # # stores it in a matrix format
        roundkey = [['a', 'b', 'c', 'd'],
                    ['e', 'f', 'g', 'h'],
                    ['i', 'j', 'k', 'l'],
                    ['m', 'n', 'o', 'p']]
        addRoundKey(roundkey, matrix)
        print("Matrix after xor with roundkey:")
        print(matrix)

main()
# sbox = {}
# makeSbox(sbox)
# getBinary('C')