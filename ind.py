import time

MAX_BUFFER_SIZE = 256
RED_T = 12
GREEN_T = 13
BLUE_T = 14

sum_of_game_id = 0

def skip(s):
    i = 0
    while i < len(s) and not s[i].isdigit():
        i += 1
    return i

def str_to_positive_int(s, index):
    num = 0
    while index < len(s) and s[index].isdigit():
        num = num * 10 + int(s[index])
        index += 1
    return num, index

def str_scan(s):
    global sum_of_game_id
    i = skip(s)
    game_id, i = str_to_positive_int(s, i)
    valid = True
    while i < len(s) and valid:
        i = skip(s[i:])
        if i >= len(s):
            break
        cube_count, i = str_to_positive_int(s, i)
        if i < len(s):
            color = s[i]
            i += 1
            if color == 'r':
                if cube_count > RED_T:
                    valid = False
            elif color == 'g':
                if cube_count > GREEN_T:
                    valid = False
            elif color == 'b':
                if cube_count > BLUE_T:
                    valid = False
            else:
                print("neco jsi podělal")
                valid = False
    return game_id if valid else 0

def main():
    global sum_of_game_id
    start = time.time()
    
    try:
        with open("cube_chall.txt", "r") as file:
            for line in file:
                game_id = str_scan(line.strip())
                sum_of_game_id += game_id
    except FileNotFoundError:
        print("nanašel se file")
        return

    elapsed_time = (time.time() - start) * 1_000_000  ## konverze do milisekund :O
    print(f"Sum: {sum_of_game_id}")
    print(f"Elapsed Time: {int(elapsed_time)}")

if __name__ == "__main__":
    main()
