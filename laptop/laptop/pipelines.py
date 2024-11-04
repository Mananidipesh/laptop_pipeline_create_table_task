# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2


class LaptopPipeline:
    def process_item(self, item, spider):
        print()
        print('laptoppipeline item' , item)
        print()
        return item
    
class save_to_data:
    def process_item(self, item, spider):
        connection = psycopg2.connect(
        dbname="flipkart_lap",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432"
    )
        
        print('this is saved to db')
        cursor = connection.cursor()
        
        create_table_query = """
        CREATE TABLE IF NOT EXISTS flipkart (
            id SERIAL PRIMARY KEY,
            title varchar,
            rating float,
            Details varchar,
            price float
        )
        """
        cursor.execute(create_table_query)
        connection.commit()

        # Insert data into a table
        insert_query = "INSERT INTO flipkart(title, rating, Details, price) VALUES(%s, %s, %s , %s)"
        data_to_insert = (item['title'],item['rating'], item['Details'], item['price'])

        cursor.execute(insert_query, data_to_insert)

        # Commit the transaction
        connection.commit()

        # Close the connection
        cursor.close()
        connection.close()
        print('data inserted successfully')


