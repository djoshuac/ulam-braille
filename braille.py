from string import ascii_lowercase

braille = [
    "100000",
    "101000",
    "110000",
    "110100",
    "100100",
    "111000",
    "101100",
    "011000",
    "011110",
    "100010",
    "101010",
    "110010",
    "110110",
    "100110",
    "111010",
    "111110",
    "101110",
    "011010",
    "011110",
    "100011",
    "101011",
    "011101",
    "110011",
    "110111",
    "100111"
]

'''
..
..
..
'''

'''
_.___
._.__
_._._
__.__

'''

def fourty_five(b):
    b = list(map(int, b))
    return [
        [0, b[1], 0, 0, 0],
        [b[0], 0, b[3], 0, 0],
        [0, b[2], 0, b[5], 0],
        [0, 0, b[4], 0, 0]
    ]

def print_45(b):
    for row in fourty_five(b):
        print("".join(map(str, row)))

def print_braille(b):
    for i in range(3):
        for j in range(2):
            c = "." if b[i*2 + j] == "1" else " "
            print(c, end="")
        print("")

for l, b in zip(ascii_lowercase, braille):
    print(l)
    print_45(b)
