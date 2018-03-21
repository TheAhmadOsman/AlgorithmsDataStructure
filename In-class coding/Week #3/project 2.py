class Championship():
	def __init__(self, _year, _winner, _loser, _win_score, _lose_score):
		self._year = 
	def __str__(self):
		return self._winner + " won in " + self._year + " by " + str(self._win_score - self._lose_score)

@property
def winner():
	return self._winne

titles = dict()

with open('mlb.txt', 'r') as sport:
	sport.readline()
	for line in sport:
		line_items = line.strip().split('\t')
		line_items[2] = line_items[2].split('-')
		print(line_items)
		c = Championship(line_items[0], line_items[1], line_items[3], line_items[2][0], line_items[2][1])
		titles[b._winner] = titles.get(b._winner, 0) + 1

#collections.counter
#setter - getter

#no need for setters - get property getters for everything else