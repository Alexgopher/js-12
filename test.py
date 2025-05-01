read_sql = open('sql/create_table_news_source_api_url.sql', 'r')
sql_file = read_sql.read()
read_sql.close()
print(sql_file)