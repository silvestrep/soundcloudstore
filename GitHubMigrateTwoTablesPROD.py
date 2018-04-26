import soundcloud
import pandas as pd 
from pandas import DataFrame
import mysql.connector
client = soundcloud.Client(client_id='XXX')
userId = 'XXX'
usersdata = client.get('/users/'+userId+'')
tracks = client.get('/users/'+userId+'/tracks')
userslist = []
trackslist = []


finaldata = userslist.append((usersdata.id,usersdata.followers_count))

conn = mysql.connector.connect(user='root', password='XXX',
                              host='127.0.0.1',
                              database='soundcloudstore')

cursor = conn.cursor()

q = """INSERT INTO Users (userid, followers) VALUES (%s,%s)"""

cursor.executemany(q, userslist)
conn.commit()

for x in tracks:
    trackslist.append((x.title, str(x.playback_count),str(x.id),str(x.favoritings_count),str(x.comment_count),str(x.user_id)))

conn = mysql.connector.connect(user='root', password='joaosoundcloudstore',
                              host='127.0.0.1',
                              database='soundcloudstore')

cursor = conn.cursor()

q = """INSERT INTO Tracks (Track_Name, Plays,TrackId,Likes,Comments,userid) VALUES (%s,%s,%s,%s,%s,%s)"""

cursor.executemany(q, trackslist)
conn.commit() 
