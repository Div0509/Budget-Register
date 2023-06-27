from django.shortcuts import render
# import mysql.connector as sql
import pymysql as sql


fn=''
ln=''
un=''
pw=''

def signaction(request):
    global uid,fn,ln,un,pw
    if request.method =='POST':
        m=sql.connect(host="localhost",user="root",password="system1234",database="mydb")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            
            if key=="firstname":
                fn=value
            if key=="lastname":
                ln=value
            if key=="username":
                un=value
            if key=="password":
                pw=value
        
        c="insert into new Values('{}','{}','{}','{}')".format(fn,ln,un,pw)
        cursor.execute(c)
        m.commit()
    return render(request,'signup_page.html')


def home(request):
    return render(request,'home.html')
    