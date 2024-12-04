def p_mine(p_mine, M, R, U, A): # simplest heuristic 
    ''' 
    M: num mines
    R: num mines remaining (not marked)
    U: num unopened cells
    A: num adjacent mines
    '''

    p_mine = {}
    # fill p_mine with -1

    p_mine = R / U
    return p_mine


def p_mine_better(p_mine, )
