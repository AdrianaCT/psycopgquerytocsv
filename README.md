# _Psycopg Query to CSV_

_This simple script extracts data from a Postgresql database and returns the results in .csv format_

## Project Setup

The following modules are required:
1. _psycopg2_: see link for installation and download instructions http://initd.org/psycopg/
2. _csv_
3. _os_
4. _datetime_

## Example:

user='<username>'
pwd='<password>'
port=1234

my_queries={ 'firstquery':'''SELECT client, sum(purchase_total) 
FROM salestable 
WHERE trunc(purchase_day)>sysdate-5 
GROUP BY client''',
'secondquery':'''SELECT DISTINCT(CASE when sum(purchase_total)>1000 then client ELSE null end)  as VIP_LIST,
FROM salestable ''' }

os.chdir('C:\Users\Me\MyResults')
queryfunction(my_queries)

