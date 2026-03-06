from gridlock import pieces
import subprocess
import datetime

def report_all_sets_of_pieces():
    ALL_PIECES = {**pieces.PIECES, **pieces.OTHER_PIECES}
    keys = list(ALL_PIECES.keys())

    quick = {}
    for k,v in ALL_PIECES.items():
        quick[k] = v.width * v.height    

    sets_of_pieces = []

    use_piece(quick, keys, sets_of_pieces)
    print(">>> Total sets of pieces:", len(sets_of_pieces))

    started = False
    pos = 0
    for ps in sets_of_pieces:
        pos += 1    
        ps = sort_largest(ps)
        # if is_in(already_solved, ps):        
        #     continue
        if not started:
            print(">>> Starting with", ps)
            started = True
        # print(f'>>> solving for {ps}')
        now = datetime.datetime.now()
        result = subprocess.run(["cmd/setsofpieces/setsofpieces.exe", ps], capture_output=True, text=True)
        # print(">>>",result.stdout.strip())
        after = datetime.datetime.now()   
        # s,n = result.stdout.split()
        # n = int(n)
        # print(f':::{s}:::{n}:::')
        print(f'{pos} {result.stdout.strip()} ({after-now})')


def use_piece(quick, keys, sets_of_pieces, state='', pos=0, area=0):
    for i in range(pos, len(keys)):
        letter = keys[i]
        if letter in state:            
            raise Exception("Already used piece: " + letter)            
        new_state = state + letter
        new_area = area + quick[letter]
        if new_area == 64:            
            sets_of_pieces.append(new_state)
        elif new_area < 64:
            use_piece(quick, keys, sets_of_pieces, new_state, i+1, new_area)
        else:
            pass  # Move on to next letter

def sort_largest(state):
    p_digits = []
    p_alphas = []
    for c in state:
        if c.isdigit():
            p_digits.append(c)
        else:
            p_alphas.append(c)
    ret = ''.join(sorted(p_digits, reverse=True)) + ''.join(sorted(p_alphas, reverse=True))
    return ret

def is_in(already,state):
    ts = sort_largest(state)
    for c in already:
        if sort_largest(c) == ts:
            return True
    return False

def top_bottom(lst, n):
    for p in lst[:n]:
        print(p)
    print("...")
    for p in lst[-n:]:
        print(p)
    print()

def report_all_sets_solutions():
    solutions = []
    no_solutions = []
    with open('setsolves.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('>'):
                continue
            pos, pieces, num_solutions, board, time = line.split()
            pos = int(pos)
            num_solutions = int(num_solutions)
            if num_solutions > 0:
                solutions.append((pieces, num_solutions, board))
            else:
                no_solutions.append(pieces)
    
    print(">>> Total sets with solutions:", len(solutions))
    print(">>> Total sets with no solutions:", len(no_solutions))

    print("----- Sorted by number of pieces in set:")
    solutions.sort(key=lambda x: len(x[0]), reverse=True)  # Sort by number of pieces in the set
    top_bottom(solutions, 10)

    print("----- Sorted by number of solutions:")
    solutions.sort(key=lambda x: x[1], reverse=True)  # Sort by number of solutions
    top_bottom(solutions, 10)

    

if __name__ == '__main__':

    # Pipe this to 'setsolves.txt'
    # report_all_sets_of_pieces()

    report_all_sets_solutions()


