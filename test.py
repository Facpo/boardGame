import hexutil
import board
import neopixel

max_x = 11
max_y = 12

pixels = neopixel.NeoPixel(board.D18, 132)

#sets led index inside grid
def ledIndexFromOffsetCoordinates(x,y):
	if y % 2 == 0:
		return y * max_x + x
	else :
		return (y + 1) * max_x - (x + 1) 

#convert back from double coordinate to offset
#used to turn leds on after calling lib functions
def offsetCoordinateFromDouble(hex):

    if hex.y % 2 == 0 :
        return [hex.x/2,hex.y]
    else :
        return [(hex.x+1)/2,hex.y]

# Filters real physical hexes from hex coordinate space.
def isOnBoard (x,y) :
	if x > max_x :
		return False
	if y > max_y :
		return False
	if y < 0 :
		return False
	if y % 2 == 0 and x < 0 :
		return False
	if y % 2 == 1 and x < -1 :
		return False
		
	return True

def neighboursOnBoard(hex) :
	actualNeighbours = []
	for neighbour in hex.neighbours() :
		if isOnBoard(neighbour.x,neighbour.y) :
			actualNeighbours.append(neighbour)
	return actualNeighbours


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

# print(grid)
print(neighboursOnBoard(grid[0][3]))
pixels[grid[0][3].led] = (255, 0, 0)
for h in neighboursOnBoard(grid[0][3]) :
    x,y = offsetCoordinateFromDouble(h)
    pixels[grid[x][y].led] =  (0, 255, 0)



# Return existing neighbours 
#generateSpawnRegion (Hex)




