import numpy as np


def make_board(livingCells,rows,cols ) :
    newArray = np.zeros(rows*cols).reshape(rows,cols)
    for cell in livingCells:
        newArray[cell] = 1
        
    print(newArray)
    return newArray

def test_theTest() :
    assert True == True

def test_make_board() :
    assert make_board({(2,0),(2,1),(2,2)}, 5, 3).tolist() == [[0,0,0],[0,0,0],[1,1,1],[0,0,0],[0,0,0]]

def next_generation(grid) :
    newArray = grid
    num_nbrs = grid[0:grid.Length - 1, 0:grid.Length - 1]

def test_next_generation():
    assert next_generation([[0,0,0],[0,0,0],[1,1,1],[0,0,0],[0,0,0]]).tolist() == [[0,0,0],[0,1,0],[0,1,0],[0,1,0],[0,0,0]]
