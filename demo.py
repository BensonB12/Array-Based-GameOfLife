
# %%
import numpy as np

grid = [[0,0,0],[0,0,0],[1,1,1],[0,0,0],[0,0,0]]

# Goal is [[2,3,2][1,2,1][2,3,2]]

print(grid[2:3] + grid[3:4])

# %%
range(10)

# %%
list(range(10))

# %%
np.array(range(10))

# %%
np.arange(12).reshape(3,4)

# %%
n = 3
m = 4
a = np.arange(n * m).reshape((n, m))

print(a * 8)

# %%
print(a * a)

# %%
# Left pad, small shape with ones
np.arange(3)+5
# %%
np.ones((3,3))+np.arange(3)

# %%
np.arange(3).reshape((3, 1))+np.arange(3)

# %%
print(np.arange(3))
# %%
print(np.arange(3).shape)
# %%
print(a)
print(a[1,2])
print(a[1][2])
print(a.reshape(2,6))
print(a.reshape(12,1))
print(a.reshape(12,))
print(a.reshape(12))
# %%
b = np.arange(12).reshape((3,4)) < 6

# %%
c = b < 6
# %%
b[c]

# %%
print(np.ones((1,3,2)))

# Tuple      a[1,2]  = a[1][2]     a[ a < 6 & a > 1] -> [5, 2, 3]

# Array languages

# %% 
aa = np.arange(2*4*3).reshape((2,4,3))
print(aa)
# %%
aa[0,1]
# %%
aa[[1,0]]
# %%
aa[[1,0],1]
# %%
aa[:,1]
# %%
aa[:,[1]]
aa[:,[1]].shape
# %%
aa[[0,1],:]

# %%
aa[[0,1],[1]]