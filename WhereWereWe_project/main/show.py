import tvdbsimple as tvdb
tvdb.KEYS.API_KEY = '491A6814F8241D30'

class Show():

	def __init__(self, id):

		self.id = id
		show = tvdb.Series(id)
		response = show.info()

	#	self.episodes = show.Episodes.all()

		self.series_episodes = tvdb.Series_Episodes(id)
		response = self.series_episodes.summary()

		self.seriesCount = max(map(int, self.series_episodes.airedSeasons))
		self.posters = show.Images.poster()
		self.series = show

	def printEpisodes(self):
		for episode in self.episodes:
			print str(episode['id']) + " : " + episode['episodeName']



