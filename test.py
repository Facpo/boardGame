import hexutil
import board
import neopixel

max_x = 11
max_y = 12

pixels = neopixel.NeoPixel(board.D18, 132)

#sets led index inside grid
def ledIndexFromOffsetCoordinates(x,y) :
	if y % 2 == 0:
		return y * max_x + x
	else :
		return (y + 1) * max_x - (x + 1) 

#convert back from double coordinate to offset
#used to turn leds on after calling lib functions
def offsetCoordinateFromDouble(hex) :

    if hex.y % 2 == 0 :
        return [hex.x/2,hex.y]
    else :
        return [(hex.x+1)/2,hex.y]

def doubleCoordinateFromOffset(x,y) :

	if y % 2 == 0 :
		newhex = hexutil.Hex(x*2, y)
	else :
		newhex = hexutil.Hex((x*2)-1, y)

	return newhex

#chooses one of side hexes at random
#returns it along with list of neighbours
def generateSpawnRegion () :
	sideChoice = random.randrange(4)
	regionHexes = []
	if sideChoice == 0 :
	#Top
		center = doubleCoordinateFromOffset(random.randrange(max_x - 1),0)

	elif sideChoice == 1 :
	#Right
		center = doubleCoordinateFromOffset(max_x - 1,random.randrange(1, max_y))

	elif sideChoice == 2 :
	#Bottom
		center = doubleCoordinateFromOffset(random.randrange(1, max_x - 1),max_y)

	else:
	#Left 
		center = doubleCoordinateFromOffset(0,random.randrange(max_y - 1))

	regionHexes = neighboursOnBoard(center)
	regionHexes.append(center)
	return regionHexes


# Filters offset coordinates that are off board
def isOnBoard (x,y) :
	if x >= max_x :
		return False
	if y >= max_y :
		return False
	if y < 0 :
		return False
	if y % 2 == 0 and x < 0 :
		return False
	if y % 2 == 1 and x < -1 :
		return False
		
	return True

# Return existing neighbours 
def neighboursOnBoard(hex) :
	actualNeighbours = []
	for neighbour in hex.neighbours() :
		offsetX,offsetY = offsetCoordinateFromDouble(neighbour)
		if isOnBoard(offsetX,offsetY) :
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


#TEST
# pixels[grid[5][5].led] = (255, 0, 0)
# for h in neighboursOnBoard(grid[5][5]) :
#     x,y = offsetCoordinateFromDouble(h)
#     pixels[grid[x][y].led] =  (0, 255, 0)

for hex in generateSpawnRegion() :

	x,y = offsetCoordinateFromDouble(hex)
	
	pixels[ledIndexFromOffsetCoordinates(x,y)] = (0, 255, 0):





