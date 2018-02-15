import tvdbsimple as tvdb
tvdb.KEYS.API_KEY = '491A6814F8241D30'

class Show():

	def __init__(self, id):
		self.id = id
		show = tvdb.Series(id)
		response = show.info()
		self.series = show
		self.seriesName = show.seriesName
		self.episodes = show.Episodes.all()
		self.posters = show.Images.poster()


	def printEpisodes(self):
		for episode in self.episodes:
			print str(episode['id']) + " : " + episode['episodeName']

