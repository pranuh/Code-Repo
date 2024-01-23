import psycopg2
from configparser import ConfigParser


#function to set a connection

def connection(link,database):                                  
    try:
        # Load the configuration file
        config = ConfigParser()
        config.read(link)

        ## Retrieve the credentials
        host = config.get(database, 'host')
        dbname = config.get(database, 'dbname')
        user = config.get(database, 'user')
        password = config.get(database, 'password')

        # Connect to the database
        conn = psycopg2.connect(
            host=host,
            dbname=dbname,
            user=user,
            password=password)
        cur = conn.cursor()
        conn.set_session(autocommit=True)
        return conn, cur
    
    except psycopg2.Error as e:
        print("Error: could not make connection")
        return print(e)

#Fetching data from the database

def query_to_df(sql_query):
    cur.execute(sql_query)
    columns = [desc[0] for desc in cur.description]
    df = pd.DataFrame(cur.fetchall(),columns=columns)
    return df  

link = "C:/Users/pranuh/Desktop/Jupyter/8 week SQL challenge - Data with Danny/danny_diner.ini"
database = "danny_diner"

conn,cur = connection(link,database)

cur.close()          #closing old connections
conn.close()

def create_table(query):                     #function to create a table
    try:
        cur.execute(query)
        print("Table created successfully!")
        return 
    except psycopg2.Error as e:
        print("Error: Creating table")
        return print(e)

def insert_table_df(df,query):                         # Function to insert a dataframe
    data= df.values.tolist()
    try:
        for row in data:
            cur.execute(query,row)
        print("Inserted data successfully!")
        return 
    except psycopg2.Error as e:
        print("Error: while loading the data")
        print(e)

def insert_data(query):                            #function to insert data
    try:
        cur.execute(query)
        conn.commit()
        print("Record inserted successfully")
    except psycopg2.Error as e:
        print("Error inserting record")
        print(e)

#function to convert sql query to df

def query_to_df(sql_query):
    cur.execute(sql_query)
    columns = [desc[0] for desc in cur.description]
    df = pd.DataFrame(cur.fetchall(), columns=columns)
    return df

# Execute the SQL query to retrieve the list of databases
cur.execute("SELECT datname FROM pg_database")

# Fetch all rows from the result set
rows = cur.fetchall()

# Print the list of databases
for row in rows:
    print(row[0])

# Execute the SQL query to retrieve the list of tables
cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")

# Fetch all rows from the result set
rows = cur.fetchall()

# Print the list of databases
for row in rows:
    print(row[0])
