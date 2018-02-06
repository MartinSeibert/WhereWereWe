import tvdbsimple as tvdb
tvdb.KEYS.API_KEY = '491A6814F8241D30'

#search = tvdb.Search()
#reponse = search.series("attack on titan")

#print search.series[0]['id']

#show = tvdb.Series(search.series[0]['id'])

#response = show.info()


#print show.seriesName

#episodes = show.Episodes.all()

#for episode in episodes:
#	print str(episode['id']) + " : " + episode['episodeName']

#ep = tvdb.Episode(episodes[0]['id'])

#response = ep.info()

#print "Season " + str(ep.airedSeason)
#print "Episode " + str(ep.airedEpisodeNumber)


class Show():

	def __init__(self, id):
		self.id = id
		show = tvdb.Series(id)
		response = show.info()
		self.seriesName = show.seriesName
		self.episodes = show.Episodes.all()

	def printEpisodes(self):
		for episode in self.episodes:
			print str(episode['id']) + " : " + episode['episodeName']







show = Show(267440)

#show.printEpisodes()

print show.episodes[1]['episodeName']