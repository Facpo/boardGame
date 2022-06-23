import hexutil
import board
import neopixel

max_x = 11
max_y = 12

pixels = neopixel.NeoPixel(board.D18, 132)

def ledIndexFromOffsetCoordinates(x,y):
	if y % 2 == 0:
		return y * max_x + x
	else :
		return (y + 1) * max_x - (x + 1) 

def offsetCoordinateFromDouble(hex):

    if hex.y % 2 == 0 :
        return [hex.x,hex.y/2]
    else :
        return [hex.x,(hex.y+1)/2]

# Master Grid that will holds all Hexes using offset coordinate system. I Rows, J Columns
grid = {} 
for x in range(0, max_x) :
	col = {}
	for y in range(0, max_y) : 	
		if y % 2 == 0 :
			newhex = hexutil.Hex(x*2, y)
		else :
			newhex = hexutil.Hex((x*2)-1, y)
		newhex.led = ledIndexFromOffsetCoordinates(x, y)
		col[y] = newhex
	grid[x] = col

print(grid)

pixels[grid[1][3].led] = (255, 0, 0)
for h in grid[1][3].neighbours() :
    x,y = offsetCoordinateFromDouble(h)
    pixels[grid[x][y].led] =  (0, 255, 0)


# Filters real physical hexes from hex coordinate space.
#isOnBoard (i,j) 

# Return existing neighbours 
#generateSpawnRegion (Hex)




