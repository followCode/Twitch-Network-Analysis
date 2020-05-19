DOTA_nodes_label=set([])	#label because we just need to count
AC_COD_nodes_label=set([])
COD_nodes_label = set([])

streamers = set([])
users = set([])

isFile = False

node_file = None
edge_file = None

if isFile:
	node_file = open("../../../college/SNA_DATA/demo/moba_shooter_simulation_node.csv", "w")
	node_file.write("Id,Label,category\n")
	edge_file = open("../../../college/SNA_DATA/demo/moba_shooter_simulation_edge.csv", "w")
	edge_file.write("Source,Target,game\n")


for i in g.edges:
	if i.game=="DOTA":
		DOTA_nodes_label.add(i.source.label)
		if isFile:
			users.add(i.source.label)
			streamers.add(i.target.label)
			edge_file.write(""+i.source.label+","+i.target.label+",DOTA\n")
	elif i.game=="AC" or i.game=="COD":
		AC_COD_nodes_label.add(i.source.label)
		if isFile:
			users.add(i.source.label)
			streamers.add(i.target.label)
			if i.game=="AC":
				edge_file.write(""+i.source.label+","+i.target.label+",AC\n")
			elif i.game=="COD":
				edge_file.write(""+i.source.label+","+i.target.label+",COD\n")


com_sources_label= DOTA_nodes_label.intersection(AC_COD_nodes_label)

print("Total users who watch DOTA: ", len(DOTA_nodes_label))
print("No of users who watch DOTA and also watch AC or COD: ",len(com_sources_label))

print("Probability that a user watches AC or COD given that he watches DOTA: %.4f"%(float(len(com_sources_label))/float(len(DOTA_nodes_label))))

if isFile:
	# Add streamers to node list
	for streamer in streamers:
		node_file.write(""+streamer+","+streamer+",streamer\n")
	for user in users:
		node_file.write(""+user+","+user+",user\n")

if isFile:
	node_file.close()
	edge_file.close()
