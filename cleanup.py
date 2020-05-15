import os

games = os.listdir("games/")

f2 = open("clean/data_edge_30s_25v.csv", "w")
f2.write("Source,Target,game\n")
f2.close()

f2 = open("clean/data_node_30s_25v.csv", "w")
f2.write("Id,Label,category\n")
f2.close()

users = set()
streamers = set()

for game in games:
    f1 = open("games/"+game, "r")
    streamerCount = 0
    userCount = 0
    with open("clean/data_edge_30s_25v.csv", "a") as f:
        for line in f1:
            line = line.split()
            if line[1] not in streamers:
                streamerCount+=1
                userCount = 0
                if streamerCount==3:
                    break
                streamers.add(line[1])
            userCount+=1
            if userCount<5001:
                users.add(line[0])
                n_line = "{0},{1},{2}\n".format(line[0], line[1], game)
                f.write(n_line)

with open("clean/data_node_30s_25v.csv", "a") as f:
    for streamer in streamers:
        f.write("{0},{0},streamer\n".format(streamer))

    for user in users:
        f.write("{0},{0},user\n".format(user))

print("[LOG] Completed creating!")

