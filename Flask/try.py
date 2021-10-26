import urllib.request
import re
from bs4 import BeautifulSoup
value = 10
for x in range(6):
	data=urllib.request.urlopen("https://api.thingspeak.com/update?api_key=M3P61VAHIEC6W395&field1="+str(value));
	value = value + 10;
	print(value);


# datafromwebsite=urllib.request.urlopen("https://api.thingspeak.com/channels/9/fields/1.xml?results=100&median=10");
# print(datafromwebsite)
# select=repr(datafromwebsite.read());
# # print(select)
# with open("a.txt","w") as f:
# 	f.write(select)





# select=select[300:];

# pick=re.search('field1":"(.+?)"',select);
# print(pick)
# if pick:
#  pick.group(1).split();


# b'{"channel":{"id":1178399,"name":"Soil Monitor","latitude":"0.0","longitude":"0.0","field1":"soil sensor 1","created_at":"2020-10-08T06:29:45Z","updated_at":"2021-05-24T09:52:58Z","last_entry_id":81},
# "feeds":[{"created_at":"2021-05-04T05:21:56Z","entry_id":72,"field1":"54\\r\\n"},
# {"created_at":"2021-05-04T05:22:13Z","entry_id":73,"field1":"54\\r\\n"},
# {"created_at":"2021-05-04T05:22:29Z","entry_id":74,"field1":"54\\r\\n"},
# {"created_at":"2021-05-04T05:22:46Z","entry_id":75,"field1":"54\\r\\n"},
# {"created_at":"2021-05-04T05:23:03Z","entry_id":76,"field1":"54\\r\\n"},
# {"created_at":"2021-05-04T05:23:20Z","entry_id":77,"field1":"54\\r\\n"},
# {"created_at":"2021-05-04T05:23:36Z","entry_id":78,"field1":"54\\r\\n"},
# {"created_at":"2021-05-04T05:23:53Z","entry_id":79,"field1":"54\\r\\n"},
# {"created_at":"2021-05-04T05:24:10Z","entry_id":80,"field1":"54\\r\\n"},
# {"created_at":"2021-05-04T05:24:26Z","entry_id":81,"field1":"54\\r\\n"}]}'