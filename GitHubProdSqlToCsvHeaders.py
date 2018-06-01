import pymysql
import pandas as pd 


db_connection = pymysql.connect(user='root', password='XXX',
                              host='127.0.0.1',
                              database='soundcloudstore')



df = pd.read_sql('select a.Track_Name,a.Plays,a.Likes, a.EventDateTime from  soundcloudstore.Tracks a inner join (select Max(EventDateTime) as Latest from soundcloudstore.Tracks) b on a.EventDateTime = b.Latest;',con=db_connection)


df.to_csv("./soundcloud_d3/HTML_Templates/ProdFiles/TotalPlaysLikesPandas.csv")

