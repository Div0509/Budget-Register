from django.shortcuts import render
from django.db import connection
import pymysql as sql

sr=''
dt=''
dp=''
pa=''
pav=''
pn=''
bl=''

def newrecord(request):
    global dp,pa,pav,pn
    if request.method =='POST':
        m = sql.connect(host="localhost",user="root",password="system1234",database="mydb")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            
            if key=="Description_of_proposal":
                dp=value
            if key=="Proposal_Amount":
                pa=value
            if key=="Provision_Availed":
                pav=value
            if key=="Party_Name":
                pn=value
            
        c="insert into itdepartment(Description_of_proposal, Proposal_Amount, Provision_Availed, Party_Name) Values('{}','{}','{}','{}')".format(dp,pa,pav,pn)
        cursor.execute(c)
        m.commit()
    return render(request,'newrecord.html')
    





