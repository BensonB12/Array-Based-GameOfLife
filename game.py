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

# def test_next_generation():
#     assert next_generation([[0,0,0],[0,0,0],[1,1,1],[0,0,0],[0,0,0]]).tolist() == [[0,0,0],[0,1,0],[0,1,0],[0,1,0],[0,0,0]]



a = np.array([[0,0,0],[0,0,0],[1,1,1],[0,0,0],[0,0,0]])

#getting the counts of neighbor cells array
def create_counts_board(grid):
    n,m = grid.shape
    right = slice(0,n),slice(1,m)
    upperright = slice(0,n-1),slice(1,m)
    upper = slice(0,n-1),slice(0,m)
    upperleft = slice(0,n-1),slice(0,m-1)
    left = slice(0,n),slice(0,m-1)
    lowerleft = slice(1,n),slice(0,m-1)
    lower = slice(1,n),slice(0,m)
    lowerright = slice(1,n),slice(1,m)

    newArray = np.zeros((n,m))

    newArray[left] = grid[right]
    newArray[upperright] += grid[lowerleft]
    newArray[upper] += grid[lower]
    newArray[upperleft] += grid[lowerright]
    newArray[lowerleft] += grid[upperright]
    newArray[lower] += grid[upper]
    newArray[lowerright] += grid[upperleft]
    newArray[right] += grid[left]


    #use if statements to check if alive
    #willLive = (count ==2) & (grid ==1) 1 | (count ==3)
    #if alive and count is 2 or 3 keep alive

    #if dead check if 3, make alive, else dead


    return newArray

myArray = create_counts_board(a)
print(myArray)


def test_create_counts_board():

    assert create_counts_board(np.array([[0,0,0],[0,0,0],[1,1,1],[0,0,0],[0,0,0]])).tolist() == [[0, 0, 0,], [2, 3, 2,], [1, 2, 1,], [2, 3, 2,], [0, 0, 0,]]