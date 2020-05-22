# Twitch-Network-Ananlysis

## Abstract

Twitch is a well-established live streaming platform with a large number of viewers and content
creators that regularly make content for the site. The platform has a variety content and various
games climb up and down the most watched section channels. We collected data about user and
streamers "follow" data to identify current user interests in trending games, streamer content and
following behavior. With the collected information, our goal is to analyze the variety of content
genres of the top channels and the impact of users following streamers on the viewership and the
generated content on the platform. We use Gephi and Python to visualize the diversity in the content
produced on the platform and to gauge the probability of a new users watching similar or entirely
different content based on their current following habits and previous user data.

## Data Description

The data was collected during the end of the month of April till the beginning of the month of May
directly from Twitch.tv using the Twitch REST API. The collected data is of the top fifteen games
from the specified time period. The games are spread across twelve genres mainly consisting the
mostly viewed genres. For each of the top fifteen games, data is collected for the top two streamers.
The resulting data is for around hundred and fifty users and thirty streamers.

Node List:

![Node List](https://github.com/followCode/Twitch-Network-Analysis/blob/master/out1.png)

Edge List:

![Edge List](https://github.com/followCode/Twitch-Network-Analysis/blob/master/out2.png)


## Graph Build Details

### Tools Used

The graph has been visualized and analyzed using Gephi. The queries regarding the graph were a
little complex and the filters available in the Gephi were not able to satisfy the queries directly.
Therefore preprocessing of nodes and edges was required to generate subgraphs for the queries
and has been done with the help of python. Python has also been used for analysis of the generated
subgraphs.



