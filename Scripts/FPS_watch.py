FPS_nodes_label = set([])
userCount = len(g.nodes)-30

for i in g.edges:
	if i.game=="COD" or i.game=="CSGO" or i.game=="FORT" or i.game=="AL":
		FPS_nodes_label.add(i.source.label)

print("Total users: ", str(userCount))
print("No of users who watch FPS: ",len(FPS_nodes_label))

perc = (float(len(FPS_nodes_label))/float(userCount))*100

print("Probability to watch FPS: %.4f"%perc)

