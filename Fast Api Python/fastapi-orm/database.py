from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


#Local mysql connection string
mysql_database_url='mysql+pymysql://root:root@localhost/dbone'

#establish database connection

engine=create_engine(mysql_database_url)

#to execute / perform crud operations

SessionLocal= sessionmaker(autocommit=False, bind=engine, autoflush=False)

#to create database sql table

Base=declarative_base()