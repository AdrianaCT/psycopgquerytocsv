# _Psycopg Query to CSV_

This simple script extracts data from a Postgresql database and returns the results in .csv format_

## Project Setup

The following modules are required:
1. _psycopg2_: see link for installation and download instructions http://initd.org/psycopg/ \n
2. _csv_ \n
3. _os_ \n
4. _datetime_ \n

## Example:

user='username' \n
pwd='password'\n
port=1234\n

my_queries={ 'firstquery':'''SELECT client, sum(purchase_total) 
FROM salestable 
WHERE trunc(purchase_day)>sysdate-5 
GROUP BY client''', \n
'secondquery':'''SELECT DISTINCT(CASE when sum(purchase_total)>1000 then client ELSE null end)  as VIP_LIST,
FROM salestable ''' }

os.chdir('C:\Users\Me\MyResults')\n
queryfunction(my_queries)

