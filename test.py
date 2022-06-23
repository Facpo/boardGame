import hexutil
import board
import neopixel


pixels = neopixel.NeoPixel(board.D18, 132)

def ledIndexFromOffsetCoordinates(i,j):
	if i % 2 == 0:
		return i * max_cols + j
	else :
		return (i + 1) * max_cols - (j + 1) 

def offsetCoordinateFromDouble(hex):

    if hex.y % 2 == 0 :
        return [hex.x,hex.y/2]
    else :
        return [hex.x,(hex.y+1)/2]

max_rows = 12
max_cols = 11

# Master Grid that will holds all Hexes using offset coordinate system. I Rows, J Columns
grid = {} 

for i in range(0,12) : 
	row = {}
	for j in range(0,11) :
		if i % 2 == 0 :
			# print (i)
			# print (j*2)
			# print ("\n")
			newhex = hexutil.Hex(j*2,i)
		else :
			# print (i)
			# print ((j*2)-1)
			# print ("\n")
			newhex = hexutil.Hex((j*2)-1,i)
		newhex.led = ledIndexFromOffsetCoordinates(i,j)
		row[j] = newhex
		grid[i] = row

#print(grid[1][3].led)

pixels[grid[1][3].led] = (255, 0, 0)
for h in grid[1][3].neighbours() :
    i,j = offsetCoordinateFromDouble(h)
    pixels[grid[i][j].led] =  (0, 255, 0)


# Filters real physical hexes from hex coordinate space.
#isOnBoard (i,j) 

# Return existing neighbours 
#generateSpawnRegion (Hex)




