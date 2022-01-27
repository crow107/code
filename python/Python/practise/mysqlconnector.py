import mysql.connector
conn=mysql.connector.connect(user='root',passwd='kanishk',host='localhost',database='kanishk')
a=conn.cursor()
k="INSERT INTO students(rollno,class,sname,DOB,city)VALUES({},'{}','{}','{}','{}')".format(7,'12-a','ram','2003-05-21','new delhi')

a.execute(k)
conn.commit()
