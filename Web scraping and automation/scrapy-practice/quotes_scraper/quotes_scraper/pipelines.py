# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# Scraped data -> Item containers -> Json/csv files
# Scraped data -> Item Containers -> Pipeline -> SQL/Mongo database
import sqlite3


class QuotetutorialPipeline(object):
    def __init__(self):
        self.connection, self.cursor = self.create_db()
        self.create_table()

    def create_db(self):
        self.connection = sqlite3.connect("quotes.db")
        self.cursor = self.connection.cursor()
        return self.connection, self.cursor

    def create_table(self):
        try:
            self.cursor.execute("""CREATE TABLE quotes(
                            quote text unique,
                            author text,
                            tags text)
                            """)
        except:
            pass

    def process_item(self, item, spider):
        self.store_data(item)
        return item

    def store_data(self, item):
        tags = [f"{tag}, " for tag in item['tags'][:]]
        tags = "".join(tags)
        self.cursor.execute("""INSERT INTO quotes values  (?, ?, ?)""",
                            (item['quote'][0], item['author'][0], tags))
        self.connection.commit()
