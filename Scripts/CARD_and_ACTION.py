card_source=set([])
action_source=set([])
AC=[]
COD=[]
union=[]

isFile = False

node_file = None
edge_file = None
if isFile:
	node_file = open("../../../college/SNA_DATA/demo/card_and_action_node.csv", "w")
	node_file.write("Id,Label,category\n")
	edge_file = open("../../../college/SNA_DATA/demo/card_and_action_edge.csv", "w")
	edge_file.write("Source,Target,game\n")

streamers = set([])
users = set([])

for i in g.edges:
	if i.game=="HRTSTN":
		#AC.append(i)
		card_source.add(i.source.label)
		union.append(i)
		streamers.add(i.target.label)
	elif i.game=="GTA":
		#COD.append(i)
		action_source.add(i.source.label)
		union.append(i)
		streamers.add(i.target.label)

com_sources= card_source.intersection(action_source)

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

print("Number of people who watch both: %d"%len(users))
if isFile:
	node_file.close()
	edge_file.close()