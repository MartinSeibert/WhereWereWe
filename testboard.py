#https://pythonhosted.org/pytvdbapi/examples.html#basic-usage

from pytvdbapi import api
db = api.TVDB("B43FF87DE395DF56")
result = db.search("Attack on titan", "en")

# If there's a perfect match, the result will be in the 0th element
# If not, the results will be in the order in which they may match so you could search for A or something

print result


show = result[0]

# dir shows all of the attributes available
print dir(show)

# "Update" pulls all of the data in from the API, before you do this, the show object is incomplete. You also have to call load_actors() and load_banners to load that stuff

show.update()

''' Attributes: 
['Actors', 'Airs_DayOfWeek', 'Airs_Time', 'AliasNames',
 'ContentRating', 'FirstAired', 'Genre', 'IMDB_ID', 'Language',
 'Network', 'NetworkID', 'Overview', 'Rating', 'RatingCount', 'Runtime',
 'SeriesID', 'SeriesName', 'Status', 'actor_objects', 'added', 'addedBy',
 'api', 'banner', 'banner_objects', 'fanart', 'id', 'lang', 'language',
 'lastupdated', 'poster', 'seriesid', 'tms_wanted_old', 'zap2it_id']
 '''

print(show.SeriesName)
print(show.FirstAired)

for season in show:
	print (season.season_number)
	print ("SEASON Length: " + str(len(season)))

	for episode in season:
		print(episode.EpisodeName)

		
# seasons are accessible through the iterators on the show object
season_1 = show[1]
print dir(season_1)
print season_1.show