# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
# Scraped data -> Item containers -> Json/csv files
# Scraped data -> Item Containers -> Pipeline -> SQL/Mongo database
import sqlite3

import mysql.connector

PASSWORD = os.environ.get('PASSWORD')


class QuotetutorialPipeline(object):
    def __init__(self):
        self.connection, self.cursor = self.create_sqlite_db()
        # self.connection, self.cursor = self.create_mysql_db()
        self.create_table()

    def create_sqlite_db(self):
        self.connection = sqlite3.connect("quotes.db")
        self.cursor = self.connection.cursor()
        return self.connection, self.cursor

    def create_mysql_db(self):
        self.connection = mysql.connector.connect(
            host="127.0.0.1",
            port="3306",
            user="root",
            password=PASSWORD,
            auth_plugin='mysql_native_password',
            database='quotes')
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

    def store_data_mysql(self, item):
        tags = [f"{tag}, " for tag in item['tags'][:]]
        tags = "".join(tags)
        self.cursor.execute("""INSERT INTO quotes values  (%s, %s, %s)""",
                            (item['quote'][0], item['author'][0], tags))
        self.connection.commit()

    def process_item(self, item, spider):
        self.store_data(item)
        # self.store_data_mysql(item)
        return item

    def store_data(self, item):
        tags = [f"{tag}, " for tag in item['tags']]
        tags = "".join(tags)
        self.cursor.execute("""INSERT INTO quotes values  (?, ?, ?)""",
                            (item['quote'][0], item['author'][0], tags))
        self.connection.commit()
