

DOTA_nodes_label=set([])	#label because we just need to count
AC_nodes_label=set([])	


for i in g.edges:
	if i.game=="DOTA":
		COD_nodes_label.add(i.source.label)
        elif i.game=="AC":
		AC_nodes_label.add(i.source.label)


com_sources_label= DOTA_nodes_label.intersection(AC_nodes_label)

print("Total users who watch DOTA: ", len(DOTA_nodes_label))
print("No of users who watch DOTA and also watch AC: ",len(com_sources_label))

print("Probability that a user watches AC given that he watches DOTA: ", len(com_sources_label)/len(DOTA_nodes_label))

