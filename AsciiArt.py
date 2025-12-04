import os

# Color codes for console
GREEN = '\033[92m'
YELLOW = '\033[93m'
WHITE = '\033[97m'
RESET = '\033[0m'

# Function to clear console
def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Width and height of each ASCII character
CHAR_WIDTH = 12
CHAR_HEIGHT = 10

# List containing ASCII art for A-Z and 0-9 sequentially (total 36 elements)
ascii_chars = [
    # A
    ["     A     ","    A A    ","   A   A   ","  AAAAAAA  ","  A     A  "," A       A "," A       A ","           ","           ","           "],
    # B
    [" BBBBBB   "," B     B  "," B     B  "," BBBBBB   "," B     B  "," B     B  "," BBBBBB   ","          ","          ","          "],
    # C
    ["  CCCCC  "," C     C "," C       "," C       "," C       "," C     C ","  CCCCC  ","         ","         ","         "],
    # D
    [" DDDDD   "," D    D  "," D     D "," D     D "," D     D "," D    D  "," DDDDD   ","         ","         ","         "],
    # E
    [" EEEEEEE "," E       "," E       "," EEEEEE  "," E       "," E       "," EEEEEEE ","         ","         ","         "],
    # F
    [" FFFFFFF "," F       "," F       "," FFFFFF  "," F       "," F       "," F       ","         ","         ","         "],
    # G
    ["  GGGGG  "," G     G "," G       "," G  GGG  "," G     G "," G     G ","  GGGGG  ","         ","         ","         "],
    # H
    [" H     H "," H     H "," H     H "," HHHHHHH "," H     H "," H     H "," H     H ","         ","         ","         "],
    # I
    [" IIIIIII ","    I    ","    I    ","    I    ","    I    ","    I    "," IIIIIII ","         ","         ","         "],
    # J
    [" JJJJJJJ ","      J  ","      J  ","      J  ","      J  "," J    J  ","  JJJJ   ","         ","         ","         "],
    # K
    [" K    K  "," K   K   "," K  K    "," KKK     "," K  K    "," K   K   "," K    K  ","         ","         ","         "],
    # L
    [" L       "," L       "," L       "," L       "," L       "," L       "," LLLLLLL ","         ","         ","         "],
    # M
    [" M     M "," MM   MM "," M M M M "," M  M  M "," M     M "," M     M "," M     M ","         ","         ","         "],
    # N
    [" N     N "," NN    N "," N N   N "," N  N  N "," N   N N "," N    NN "," N     N ","         ","         ","         "],
    # O
    ["  OOOO  "," O    O "," O    O "," O    O "," O    O "," O    O ","  OOOO  ","         ","         ","         "],
    # P
    [" PPPPPP  "," P     P "," P     P "," PPPPPP  "," P       "," P       "," P       ","         ","         ","         "],
    # Q
    ["  QQQQ  "," Q    Q "," Q    Q "," Q    Q "," Q  Q Q "," Q   Q  ","  QQQ Q ","         ","         ","         "],
    # R
    [" RRRRRR  "," R     R "," R     R "," RRRRRR  "," R   R   "," R    R  "," R     R ","         ","         ","         "],
    # S
    ["  SSSSS "," S     S"," S      ","  SSSSS ","       S"," S     S","  SSSSS ","        ","        ","        "],
    # T
    [" TTTTTTT ","    T    ","    T    ","    T    ","    T    ","    T    ","    T    ","         ","         ","         "],
    # U
    [" U     U "," U     U "," U     U "," U     U "," U     U "," U     U ","  UUUUU  ","         ","         ","         "],
    # V
    [" V     V "," V     V "," V     V ","  V   V  ","   V V   ","    V    ","         ","         ","         ","         "],
    # W
    [" W     W "," W     W "," W  W  W "," W  W  W "," W W W W "," W W W W ","  W   W  ","         ","         ","         "],
    # X
    [" X     X ","  X   X  ","   X X   ","    X    ","   X X   ","  X   X  "," X     X ","         ","         ","         "],
    # Y
    [" Y     Y ","  Y   Y  ","   Y Y   ","    Y    ","    Y    ","    Y    ","    Y    ","         ","         ","         "],
    # Z
    [" ZZZZZZZ ","      Z  ","     Z   ","    Z    ","   Z     ","  Z      "," ZZZZZZZ ","         ","         ","         "],
    # 0
    ["  0000  "," 0    0 ","0      0","0      0","0      0","0      0"," 0    0 ","  0000  ","         ","         "],
    # 1
    ["    1   ","   11   ","  1 1   ","    1   ","    1   ","    1   ","  11111 ","         ","         ","         "],
    # 2
    [" 22222  ","     2  ","     2  "," 22222  "," 2      "," 2      "," 22222  ","         ","         ","         "],
    # 3
    [" 33333  ","     3  ","     3  ","  3333  ","     3  ","     3  "," 33333  ","         ","         ","         "],
    # 4
    [" 4   4  "," 4   4  "," 4   4  "," 44444  ","     4  ","     4  ","     4  ","         ","         ","         "],
    # 5
    [" 55555  "," 5      "," 5      "," 55555  ","     5  ","     5  "," 55555  ","         ","         ","         "],
    # 6
    ["  6666  "," 6      "," 6      "," 66666  "," 6    6 "," 6    6 ","  6666  ","         ","         ","         "],
    # 7
    [" 77777  ","     7  ","    7   ","   7    ","  7     "," 7      "," 7      ","         ","         ","         "],
    # 8
    ["  8888  "," 8    8 "," 8    8 ","  8888  "," 8    8 "," 8    8 ","  8888  ","         ","         ","         "],
    # 9
    ["  9999  "," 9    9 "," 9    9 ","  99999 ","      9 ","      9 ","  9999  ","         ","         ","         "]
]

# Mapping characters to index in list
def char_to_index(c):
    if 'A' <= c <= 'Z':
        return ord(c) - ord('A')
    elif '0' <= c <= '9':
        return ord(c) - ord('0') + 26
    else:
        return None

# Display colorful title
def show_title():
    print(f"{GREEN}ASCII{YELLOW} ART {WHITE}GENERATOR{RESET}")
    print("="*30)

# Main loop
while True:
    clear_console()
    show_title()
    
    name = input("Enter your name (A-Z, 0-9 only): ").upper()
    
    for row in range(CHAR_HEIGHT):
        line = ""
        for char in name:
            idx = char_to_index(char)
            if idx is not None:
                line += ascii_chars[idx][row] + "  "
            else:
                line += " " * CHAR_WIDTH + "  "
        print(line)
    
    cont = input("\nDo you want to continue? (y/n): ").lower()
    if cont != 'y':
        break
