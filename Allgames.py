subgraph= g.filter(degree>2) # I have considered 3 games in total

AC_sources=set([])
COD_sources=set([])
DOTA_sources= set([])

for i in subgraph.edges:
	if i.game=="AC":
		AC_sources.add(i.source.label)
	elif i.game=="COD":
		COD_sources.add(i.source.label)
	elif i.game=="DOTA":
		DOTA_sources.add(i.source.label)

com_sources= AC_sources.intersection(COD_sources)
com_sources= com_sources.intersection(DOTA_sources)

print("No of users who watch AC and COD and DOTA: ",len(com_sources))