import mysql.connector
import sys
import os
import traceback

ENDPOINT=os.environ['ENDPOINT']
PORT=os.environ['PORT']
USER=os.environ['USER']
PWD=os.environ['PWD']
DBNAME=os.environ['DBNAME']
os.environ['LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN'] = '1'

# If you want to use IAM AUTH

# session = boto3.Session(profile_name='default')
# client = session.client('rds')
# token = client.generate_db_auth_token(DBHostname=ENDPOINT, Port=PORT, DBUsername=USER, Region=REGION)

def lambda_handler(event, context):
    try:
        conn =  mysql.connector.connect(host=ENDPOINT, user=USER, passwd=PWD, port=PORT, database=DBNAME, ssl_ca='SSLCERTIFICATE')
        cur = conn.cursor()
        cur.execute("""SELECT now()""")
        query_results = cur.fetchall()
        print(query_results)
    except Exception as e:
        print("Database connection failed due to {}".format(e))          
        traceback.print_exc()
                    