valOne = input("Are you inputting level (1) or xp (2) for starting?: ")
xpStart = 0.0
levelStart = 0
if valOne == "1":
    levelStart = int(input("What is your archaeology level?: "))
else:
    xpStart = float(input("What is your archaeology xp?: "))

valTwo = input("Are you inputting level (1) or xp (2) for ending?: ")
xpEnd = 0.0
levelEnd = 0
if valTwo == "1":
    levelEnd = int(input("What archaeology level?: "))
else:
    xpEnd = float(input("What archaeology xp?: "))

tomes = [0,300,331.2,369.6,408,447.6,499.2,590.4,609.6,932.4,736.8,816,902.4,986.4,1099.20,1209.60,1255.20,1315.20,1368,1430.40,1488,1557.60,1617.60,1689.60,1764,1843.20,1915.20,1945.20,1987.20,2174.40,2270.40,2367.60,2467.20,2572.80,2684.40,2798.40,2920.80,3048,3177.60,3319.20,3458.40,3609.60,3765.60,3926.40,4096.80,4269.60,4459.20,4658.40,4860,5064,5284.80,5511.60,5760,5997.60,6261.60,6537.60,6825.60,7128,7420.80,7759.20,8084.40,8436,8810.40,9174,9621.60,10118.40,10423.20,11419.20,11856,12445.20,12926.40,13484.40,14143.20,14793.60,15426,16029.60,16776,17504.40,18202.80,19104,19996.80,20868,21704.40,22857.60,23608.80,24158.40,25802.40,26844,28428,29383.20,30968,31750,33257,34733,36156,38710,40068,41290,43299,45002,46704,48407,50110,51812,53515,55217,56920,58622,60325,62028,63730,65432,67135,68837,70539.50,72242,73944.50,75647,77351,80261,86561]

xp = [0,0,83,174,276,388,512,650,801,969,1154,1358,1584,1833,2107,2411,2746,3115,3523,3973,4470,5018,5624,6291,7028,7842,8740,9730,10824,12031,13363,14833,16456,18247,20224,22406,24815,27473,30408,33648,37224,41171,45529,50339,55649,61512,67983,75127,83014,91721,101333,111945,123660,136594,150872,166636,184040,203254,224466,247886,273742,302288,333804,368599,407015,449428,496254,547953,605032,668051,737627,814445,899257,992895,1096278,1210421,1336443,1475581,1629200,1798808,1986068,2192818,2421087,2673114,2951373,3258594,3597792,3972294,4385776,4842295,5346332,5902831,6517253,7195629,7944614,8771558,9684577,10692629,11805606,13034431,14391160,15889109,17542976,19368992,21385073,23611006,26068632,28782069,31777943,35085654,38737661,42769801,47221641,52136869,57563718,63555443,70170840,77474828,85539082,94442737,104273167,115126838,127110260,140341028,154948977,171077457,188884740,200000000]

if valOne == "1":
    xpStart = xp[levelStart]

if valTwo == "1":
    xpEnd = xp[levelEnd]

xpCurr = float(xpStart)
print("xpCurr is " + str(xpCurr))
print("xpEnd is " + str(xpEnd))
tomeCount = 0

#I'll be damned if I put that formula in here.
#Thank cheesus for copy/paste
while xpCurr < xpEnd:
    #print(xpCurr)
    for x in range(len(xp)):
        if xpCurr > xp[x] or xpCurr >= 200000000:
            pass
        else:
            try:
                xpCurr += tomes[x-1]
            except:
                xpCurr += tomes[120]
            tomeCount += 1
            break

print("Tome Counter: "+str(tomeCount))