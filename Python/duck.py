import duckdb
# Function to query data from the database
def query_data(sql_query):
		# Establish a connection to the specified database
		con = duckdb.connect(database=database_path)
		
		# Execute the SQL query and fetch the results as a DataFrame
		result = con.execute(sql_query).fetchdf()
		
		# Close the database connection
		con.close()
		
		return result

#Function to perform CRUD operations on the database

def crud(sql_query):
try:
# Establish a connection to the specified database
con = duckdb.connect(database=database_path)

    # Execute the provided SQL query
    result = con.execute(sql_query)

    # Close the database connection
    con.close()

    print("Successfully executed")

except Exception as e:  # 'Exception' is the base class for all exceptions
    print("Error:", e)

#Specify the path to the directory or database file Check if the path exists

import os

path_to_delete = 'C:\\Users\\pranuh\\duckdb\\my_database2.db'

if os.path.exists(path_to_delete):
if os.path.isfile(path_to_delete):
# If it's a file, remove it
os.remove(path_to_delete)
print(f"File '{path_to_delete}' removed.")
elif os.path.isdir(path_to_delete):
# If it's a directory, remove it
os.rmdir(path_to_delete)
print(f"Directory '{path_to_delete}' removed.")
else:
print(f"Path '{path_to_delete}' does not exist.")
