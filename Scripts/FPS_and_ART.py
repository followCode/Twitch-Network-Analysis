FPS_source=set([])
ART_source=set([])
AC=[]
COD=[]
union=[]

isFile = False

node_file = None
edge_file = None
if isFile:
	node_file = open("../../../college/SNA_DATA/demo/fps_and_art_node.csv", "w")
	node_file.write("Id,Label,category\n")
	edge_file = open("../../../college/SNA_DATA/demo/fps_and_art_edge.csv", "w")
	edge_file.write("Source,Target,game\n")

streamers = set([])
users = set([])

for i in g.edges:
	if i.game=="COD" or i.game=="CSGO" or i.game=="FORT" or i.game=="AL":
		#AC.append(i)
		FPS_source.add(i.source.label)
		union.append(i)
		streamers.add(i.target.label)
	elif i.game=="ART":
		#COD.append(i)
		ART_source.add(i.source.label)
		union.append(i)
		streamers.add(i.target.label)

com_sources= FPS_source.intersection(ART_source)

if isFile:
	# Add streamers to node list
	for streamer in streamers:
		node_file.write(""+streamer+","+streamer+",streamer\n")

com_edges=[]

for i in union:
	if i.source.label in com_sources:
		com_edges.append(i)
		if isFile:
			users.add(i.source.label)
			edge_file.write(""+i.source.label+","+i.target.label+","+i.game+"\n")

if isFile:
	for user in users:
		node_file.write(""+user+","+user+",user\n")

print("Number of people who watch both FPS and ART: %d"%len(users))
if isFile:
	node_file.close()
	edge_file.close()
