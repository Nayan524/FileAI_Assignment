import sys

def disk_moves(disks, start, position, pegs, counter_clockwise, clockwise):
    if disks == 0:
        return 0
    if disks % 2:
        destination = counter_clockwise[start]
    else:
        destination = clockwise[start]
    for peg in pegs:
        if peg != start and peg != destination:
            spare = peg
            break
    if position[disks] == start:
        return disk_moves(disks - 1, start, position, pegs, counter_clockwise, clockwise)

    if position[disks] == destination:
        rest = disk_moves(disks - 1, spare, position, pegs, counter_clockwise, clockwise)
        if rest == -1:
            return -1
        return (1 << (disks - 1)) + rest
    return -1

def tower_hanoi(n, state):
    pegs = ['A', 'B', 'C']
    counter_clockwise = {'A': 'C', 'C': 'B','B': 'A'}
    clockwise = {'A': 'B','B': 'C','C': 'A'}
    position = {}
    for i in range(3):
        for disk in state[i]:
            position[disk] = pegs[i]
    if len(set(position.values())) == 1:
        return position[1] + ' 0'
    for start in pegs:
        count = disk_moves(n, start, position, pegs, counter_clockwise, clockwise)
        if count != -1 and count <= (1 << n) - 2:
            return start + ' ' + str(count)

    return 'impossible'

num_case = int(sys.stdin.readline())
for _ in range(num_case):
    state = [[int(t) for t in s.split()] for s in sys.stdin.readline().split(',')]
    n = len(state[0]) + len(state[1]) + len(state[2])
    print(tower_hanoi(n, state))
