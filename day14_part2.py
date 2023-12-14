import sys
import copy
sys.setrecursionlimit(1000000)

with open('day14_input.txt') as f:
    lines = [list(l.strip()) for l in f.readlines()]
    R = len(lines)
    C = len(lines[0])

    def simulate(grid):
        ngrid = []
        for i in range(R):
            temp = ['.'] * C
            ngrid.append(temp)

        # north
        for i in range(C):
            load = R
            count = 0
            for j in range(R):
                if grid[j][i] == '#':
                    ngrid[j][i] = '#'
                    count = 0
                    load = R - j - 1
                if grid[j][i] == 'O':
                    newj = load - count
                    assert ngrid[R - newj][i] == '.'
                    ngrid[R - newj][i] = 'O'
                    count += 1

        '''
        for x in ngrid:
            print(''.join(x))
        print("=" * 20)
        '''

        grid = copy.deepcopy(ngrid)
        for i in range(R):
            for j in range(C):
                ngrid[i][j] = '.'

        # west
        for i in range(R):
            load = C
            count = 0
            for j in range(C):
                if grid[i][j] == '#':
                    ngrid[i][j] = '#'
                    count = 0
                    load = C - j - 1
                if grid[i][j] == 'O':
                    newj = load - count
                    assert ngrid[i][C - newj] == '.'
                    ngrid[i][C - newj] = 'O'
                    count += 1

        '''
        for x in ngrid:
            print(''.join(x))
        print("=" * 20)
        '''

        grid = copy.deepcopy(ngrid)
        for i in range(R):
            for j in range(C):
                ngrid[i][j] = '.'

        # south
        for i in range(C):
            load = R
            count = 0
            for j in range(R - 1, -1, -1):
                if grid[j][i] == '#':
                    ngrid[j][i] = '#'
                    count = 0
                    load = j
                if grid[j][i] == 'O':
                    newj = load - count
                    assert ngrid[newj - 1][i] == '.'
                    ngrid[newj - 1][i] = 'O'
                    count += 1

        '''
        for x in ngrid:
            print(''.join(x))
        print("=" * 20)
        '''

        grid = copy.deepcopy(ngrid)
        for i in range(R):
            for j in range(C):
                ngrid[i][j] = '.'

        # east
        for i in range(R):
            load = C
            count = 0
            for j in range(C - 1, -1, -1):
                if grid[i][j] == '#':
                    ngrid[i][j] = '#'
                    count = 0
                    load = j
                if grid[i][j] == 'O':
                    newj = load - count
                    assert ngrid[i][newj - 1] == '.'
                    ngrid[i][newj - 1] = 'O'
                    count += 1

        '''
        for x in ngrid:
            print(''.join(x))
        print("=" * 20)
        '''

        return copy.deepcopy(ngrid)


    cnt = 0
    while cnt < 1000:
        lines = simulate(lines)

        ans = 0
        for i in range(C):
            for j in range(R):
                if lines[j][i] == 'O':
                    ans += R - j

        print(ans)

        cnt += 1

    # handcheck: cycle of 13, offset 105

