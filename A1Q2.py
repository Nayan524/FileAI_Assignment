import sys

def tower_hanoi(n, state):
    pegs = ['A', 'B', 'C']

    counter_clockwise = {
        'A': 'C',
        'C': 'B',
        'B': 'A'
    }

    clockwise = {
        'A': 'B',
        'B': 'C',
        'C': 'A'
    }
    return 'impossible'

num_case = int(sys.stdin.readline())
for _ in range(num_case):
    state = [[int(t) for t in s.split()] for s in sys.stdin.readline().split(',')]
    n = len(state[0]) + len(state[1]) + len(state[2])
    print(tower_hanoi(n, state))
