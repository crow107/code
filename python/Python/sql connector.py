import mysql.connector
n=1
b=('ram')
c=1234567890
e=0

mydb = mysql.connector.connect(host="localhost"
                               ,user="root"
                               ,password="kanishk"
                               ,database='kanishk'
                               )
cur = mydb.cursor() 
i= "INSERT INTO bill (Sno,Name,Phone_No,Amount) VALUES (%s, %s, %s, %s)"
da= (n,b,c,e)
cur.execute(i,da)
mydb.commit()


