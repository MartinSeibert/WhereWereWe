import tvdbsimple as tvdb
tvdb.KEYS.API_KEY = '491A6814F8241D30'

class Show():

	def __init__(self, id):

		self.id = id
		show = tvdb.Series(id)
		response = show.info()

		#self.seriesName = show.seriesName
		self.episodes = show.Episodes.all()
		self.posters = show.Images.poster()
		maxSeason = 0

		for episode in self.episodes:
			if episode['airedSeason'] > maxSeason:
				maxSeason = episode['airedSeason']
		self.seriesCount = maxSeason
		self.series = show

	def printEpisodes(self):
		for episode in self.episodes:
			print str(episode['id']) + " : " + episode['episodeName']



