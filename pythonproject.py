import random
when = ("Once upon a time ","A year ago",)
who=(" my family and I"," my friend and I")
where=("Chennai","Mumbai")

mode=("by car it was a ","by train it was a ")
experience=("great","superb")
activity=(" We enjoyed a lot when we explored beaches and museum and the local markets. " , " We explored the city and we begin by visting some tourist attraction like historical sites and other old monuments. ")
back=("We were unhappy when we realised that the trip is going to end soon and we have to come back to our daily life routine. ", "We all were sad after realising that the trip is going to end very soon but we were also happy that we have collected a lot of memories. ")
end=("Travelling is a form of adventure which fills us with both positive and negative memories. ","Travelling can a whole lot of fun. ")




print(random.choice(when) +random.choice(who) + " went to "+ random.choice(where) + " which is 2000km far away from my home but " +random.choice(mode)  + random.choice(experience) + " experience. " + random.choice(activity) + random.choice(back) + random.choice(end))