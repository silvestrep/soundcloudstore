import pymysql
import csv

conn = pymysql.connect(user='root', password='XXX',
                              host='127.0.0.1',
                              database='soundcloudstore')

a = conn.cursor() # starts going to the database

sql = 'select a.Track_Name,a.Plays,a.Likes, a.EventDateTime from  soundcloudstore.Tracks a inner join (select Max(EventDateTime) as Latest from soundcloudstore.Tracks) b on a.EventDateTime = b.Latest'

a.execute(sql)


file = open("./soundcloud_d3/HTML_Templates/ProdFiles/TotalPlaysLikes.csv","w") #creates a file, w stands that is going to write on that file



#./Prodfiles/TotalPlaysLikes.csv
#file = open("./uatfiles/"+Today()+".csv","w") - Use datetime module/package for this 

fieldnames = ['TrackName', 'Plays','Likes','EventDateTime'] # Gives names to the headers 
writer = csv.DictWriter(file, fieldnames=fieldnames) 
writer.writeheader()


for row in a:
	file.write(str(row[0]) + ',' + str(row[1]) + ',' + str(row[2]) + ',' + str(row[3]) + '\n'); #rows are actually the columns of the table, all have to be from the same type


	
file.close()
a.close()
conn.commit() 
