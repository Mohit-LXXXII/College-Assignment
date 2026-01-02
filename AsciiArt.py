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

# List containing ASCII art for A-Z, a-z and 0-9 sequentially (total 62 elements)
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
    # a
    ["         ","         ","  aaaa   "," a    a  "," a    a  "," a    a  ","  aaaa   ","         ","         ","         "],
    # b
    [" b       "," b       "," bbbbb   "," b    b  "," b    b  "," b    b  "," bbbbb   ","         ","         ","         "],
    # c
    ["         ","         ","  cccc   "," c       "," c       "," c       ","  cccc   ","         ","         ","         "],
    # d
    ["       d ","       d "," ddddd   "," d    d  "," d    d  "," d    d  "," ddddd   ","         ","         ","         "],
    # e
    ["         ","         ","  eeee   "," e    e  "," eeeee   "," e       ","  eeee   ","         ","         ","         "],
    # f
    ["   fff   ","  f      "," fffff   ","  f      ","  f      ","  f      ","  f      ","         ","         ","         "],
    # g
    ["         "," ggggg   "," g    g  "," g    g  "," ggggg   ","      g  "," gggg    ","         ","         ","         "],
    # h
    [" h       "," h       "," hhhh    "," h    h  "," h    h  "," h    h  "," h    h  ","         ","         ","         "],
    # i
    ["    i    ","         ","    i    ","    i    ","    i    ","    i    ","   iii   ","         ","         ","         "],
    # j
    ["       j ","         ","       j ","       j ","       j "," j    j  ","  jjj    ","         ","         ","         "],
    # k
    [" k       "," k       "," k   k   "," k  k    "," kkk     "," k  k    "," k   k   ","         ","         ","         "],
    # l
    ["    l    ","    l    ","    l    ","    l    ","    l    ","    l    ","   ll    ","         ","         ","         "],
    # m
    ["         ","         "," mmm  m  "," m m m m "," m m m m "," m m m m "," m m m m ","         ","         ","         "],
    # n
    ["         ","         "," nnnn    "," n    n  "," n    n  "," n    n  "," n    n  ","         ","         ","         "],
    # o
    ["         ","         ","  oooo   "," o    o  "," o    o  "," o    o  ","  oooo   ","         ","         ","         "],
    # p
    ["         "," pppp    "," p    p  "," p    p  "," pppp    "," p       "," p       ","         ","         ","         "],
    # q
    ["         "," qqqqq   "," q    q  "," q    q  "," qqqqq   ","      q  ","      q  ","         ","         ","         "],
    # r
    ["         ","         "," rrr     "," r   r   "," r       "," r       "," r       ","         ","         ","         "],
    # s
    ["         ","         ","  ssss   "," s       ","  sss    ","      s  "," sssss   ","         ","         ","         "],
    # t
    ["    t    ","    t    "," ttttt   ","    t    ","    t    ","    t    ","     t   ","         ","         ","         "],
    # u
    ["         ","         "," u    u  "," u    u  "," u    u  "," u    u  ","  uuuu   ","         ","         ","         "],
    # v
    ["         ","         "," v     v ","  v   v  ","  v   v  ","   v v   ","    v    ","         ","         ","         "],
    # w
    ["         ","         "," w  w  w "," w  w  w "," w w w w ","  w w w  ","   w     ","         ","         ","         "],
    # x
    ["         ","         "," x    x  ","  x  x   ","   xx    ","  x  x   "," x    x  ","         ","         ","         "],
    # y
    ["         "," y    y  "," y    y  ","  y  y   ","   yy    ","    y    "," y       ","         ","         ","         "],
    # z
    ["         ","         "," zzzzzz  ","     z   ","    z    ","   z     "," zzzzzz  ","         ","         ","         "],
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


def char_to_index(c):
    if 'A' <= c <= 'Z':
        return ord(c) - ord('A')
    elif 'a' <= c <= 'z':
        return ord(c) - ord('a') + 26
    elif '0' <= c <= '9':
        return ord(c) - ord('0') + 52
    else:
        return None

# Display colorful title
def show_title():
    print(f"{GREEN}ASCII{YELLOW} ART {WHITE}GENERATOR{RESET}")
    print("="*30)

# Display menu
def show_menu():
    print("\n--- Select Display Mode ---")
    print("1. General Display (Mix of uppercase, lowercase, numbers)")
    print("2. Single Character Display")
    print("3. Only Small Characters (lowercase only)")
    print("4. Exit")
    choice = input("\nEnter your choice (1-4): ")
    return choice

# Display single character
def display_single_char():
    char = input("\nEnter a single character (A-Z, a-z, 0-9): ")
    if len(char) > 1:
        print("Please enter only one character!")
        return
    
    idx = char_to_index(char)
    if idx is not None:
        print()
        for row in range(CHAR_HEIGHT):
            print(ascii_chars[idx][row])
    else:
        print(f"Character '{char}' not supported!")

# Display only lowercase characters
def display_small_chars():
    text = input("\nEnter text (a-z only): ").lower()
    
    # Filter only lowercase letters
    filtered_text = ''.join([c for c in text if 'a' <= c <= 'z'])
    
    if not filtered_text:
        print("No valid lowercase characters found!")
        return
    
    print()
    for row in range(CHAR_HEIGHT):
        line = ""
        for char in filtered_text:
            idx = char_to_index(char)
            if idx is not None:
                line += ascii_chars[idx][row] + "  "
            else:
                line += " " * CHAR_WIDTH + "  "
        print(line)

# Display general (mixed) characters
def display_general():
    name = input("\nEnter your name (A-Z, a-z, 0-9 allowed): ")
    
    print()
    for row in range(CHAR_HEIGHT):
        line = ""
        for char in name:
            idx = char_to_index(char)
            if idx is not None:
                line += ascii_chars[idx][row] + "  "
            else:
                line += " " * CHAR_WIDTH + "  "
        print(line)

# Main loop
while True:
    clear_console()
    show_title()
    
    choice = show_menu()
    
    if choice == '1':
        display_general()
    elif choice == '2':
        display_single_char()
    elif choice == '3':
        display_small_chars()
    elif choice == '4':
        print("\nThanks for using ASCII Art Generator!")
        break
    else:
        print("Invalid choice! Please select 1-4.")
    
    if choice in ['1', '2', '3']:
        cont = input("\nDo you want to continue? (y/n): ").lower()
        if cont != 'y':
            break
