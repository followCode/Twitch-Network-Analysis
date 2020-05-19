AC_nodes_label=set([])
COD_nodes_label = set([])

for i in g.edges:
	if i.game=="COD":
		COD_nodes_label.add(i.source.label)
	elif i.game=="AC":
		AC_nodes_label.add(i.source.label)


com_sources_label= COD_nodes_label.intersection(AC_nodes_label)

print("Total users who watch COD: ", len(COD_nodes_label))
print("No of users who watch COD and also watch AC: ",len(com_sources_label))

print("Probability that a user watches AC given that he watches COD: %.4f"%(float(len(com_sources_label))/float(len(COD_nodes_label))))

