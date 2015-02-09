#!/usr/bin/python 
# -*- coding: utf-8 -*- 

import psycopg2
from psycopg2 import extras
import csv
import datetime
import os

## function starts here
def queryfunction(querylist,db,username,pwd,port):
    print str(datetime.datetime.now())
    print 'Connecting...'
    conn=psycopg2.connect(database=db,user=username,password=pwd,host='localhost',port=port,cursor_factory=psycopg2.extras.DictCursor)
    cur=conn.cursor()
    for query in querylist:
        print 'Running this query: '+str(query)
        print str(datetime.datetime.now())
        try:
            cur.execute(querylist[query])
        except psycopg2.Error,e:
            print 'Oops. something went wrong while attempting this query: '+str(query)
            print 'Error message: '+str(e.diag.message_primary) +'\n error has been saved in errorlog.csv'
            errorlog=[datetime.datetime.now(),e.diag.severity, e.diag.message_primary]
            csvfile=open('errorlog-general.csv','ab')
            mywriter=csv.writer(csvfile, delimiter=',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
            mywriter.writerow(errorlog)
            csvfile.close()
            conn.rollback()
        else:
            results=cur.fetchall()
            desc=cur.description
            fields=[]
            csvfile=open(str(query)+'.csv','wb')
            mywriter=csv.writer(csvfile,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
            for element in desc:
                fields.append(element[0])
            mywriter.writerow(fields)
            for row in results:
                mywriter.writerow(row)
            csvfile.close()
    print 'Queries done. Closing connection...'
    cur.close()
    conn.commit()
    conn.close()
###end of function #####
#EXAMPLE:

#user='<username>'
#pwd='<password>'
#port=1234

#my_queries={ 'firstquery':'''SELECT client, sum(purchase_total) 
#FROM salestable 
#WHERE trunc(purchase_day)>sysdate-5 
#GROUP BY client''',
#'secondquery':'''SELECT DISTINCT(CASE when sum(purchase_total)>1000 then client ELSE null end)  as VIP_LIST,
#FROM salestable ''' }

#os.chdir('C:\Users\Me\MyResults')
#queryfunction(my_queries)
