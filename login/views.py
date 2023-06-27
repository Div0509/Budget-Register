from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import pymysql as sql
from django.db import connection
un=''
pw=''

def loginaction(request):
    global un,pw
    if request.method =='POST':
        m=sql.connect(host="localhost",user="root",password="system1234",database="mydb")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="username":
                un=value
            if key=="password":
                pw=value
        
        c="select * from new where username='{}' and password='{}'".format(un,pw)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,"error.html")
        else:
            cursor = connection.cursor()
            cursor.execute("SHOW TABLES")
            tables = [table[0] for table in cursor.fetchall()]

            selected_table = request.POST.get('selected_table')
            columns=[]
            rows=[]
            if selected_table:
                if selected_table == 'new':
                    cursor.execute("SELECT * FROM new")
                    rows = cursor.fetchall()
                    if rows:
                        columns = [desc[0] for desc in cursor.description]

                if selected_table == 'itdepartment':
                    cursor.execute("SELECT * FROM itdepartment")
                    rows = cursor.fetchall()
                    if rows:
                        columns = [desc[0] for desc in cursor.description]


            return render(request, 'information.html', {'tables': tables, 'selected_table': selected_table, 'columns': columns, 'rows': rows})
    return render(request,'login_page.html')

def logout_user(request):
    logout(request)
    messages.success(request,"You have been Logged out.....")
    return redirect('home')