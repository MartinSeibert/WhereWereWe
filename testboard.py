import tvdbsimple as tvdb
tvdb.KEYS.API_KEY = '491A6814F8241D30'

search = tvdb.Search()
reponse = search.series("attack on titan")
print search.series[0]['seriesName']

show = search.series[0]

print show
