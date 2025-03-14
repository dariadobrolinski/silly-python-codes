def print_box_letters(name):
    name = name.upper()
    letter_map = {
        'A': ["  A  ", " A A ", "AAAAA", "A   A", "A   A"],
        'B': ["BBBB ", "B   B", "BBBB ", "B   B", "BBBB "],
        'C': [" CCC ", "C   C", "C    ", "C   C", " CCC "],
        'D': ["DDDD ", "D   D", "D   D", "D   D", "DDDD "],
        'E': ["EEEEE", "E    ", "EEE  ", "E    ", "EEEEE"],
        'F': ["FFFFF", "F    ", "FFF  ", "F    ", "F    "],
        'G': [" GGG ", "G    ", "G  GG", "G   G", " GGG "],
        'H': ["H   H", "H   H", "HHHHH", "H   H", "H   H"],
        'I': ["IIIII", "  I  ", "  I  ", "  I  ", "IIIII"],
        'J': ["JJJJJ", "    J", "    J", "J   J", " JJJ "],
        'K': ["K   K", "K  K ", "KK   ", "K  K ", "K   K"],
        'L': ["L    ", "L    ", "L    ", "L    ", "LLLLL"],
        'M': ["M   M", "MM MM", "M M M", "M   M", "M   M"],
        'N': ["N   N", "NN  N", "N N N", "N  NN", "N   N"],
        'O': [" OOO ", "O   O", "O   O", "O   O", " OOO "],
        'P': ["PPPP ", "P   P", "PPPP ", "P    ", "P    "],
        'Q': [" QQQ ", "Q   Q", "Q   Q", "Q  Q ", " QQ Q"],
        'R': ["RRRR ", "R   R", "RRRR ", "R  R ", "R   R"],
        'S': [" SSS ", "S    ", " SSS ", "    S", " SSS "],
        'T': ["TTTTT", "  T  ", "  T  ", "  T  ", "  T  "],
        'U': ["U   U", "U   U", "U   U", "U   U", " UUU "],
        'V': ["V   V", "V   V", "V   V", " V V ", "  V  "],
        'W': ["W   W", "W   W", "W W W", "WW WW", "W   W"],
        'X': ["X   X", " X X ", "  X  ", " X X ", "X   X"],
        'Y': ["Y   Y", " Y Y ", "  Y  ", "  Y  ", "  Y  "],
        'Z': ["ZZZZZ", "   Z ", "  Z  ", " Z   ", "ZZZZZ"],
        ' ': ["     ", "     ", "     ", "     ", "     "]
    }
    
    for i in range(5):
        line = "  ".join(letter_map[char][i] for char in name if char in letter_map)
        print(line)

if __name__ == "__main__":
    user_input = input("Enter a name: ")
    print_box_letters(user_input)
