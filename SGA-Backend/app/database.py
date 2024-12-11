from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from os.path import join, dirname
from dotenv import load_dotenv
import urllib.parse

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')
PORT = int(os.getenv('PORT'))
DATABASE = os.getenv('DATABASE')

params = urllib.parse.quote_plus(
    f'DRIVER={{ODBC Driver 18 for SQL Server}};'
    f'SERVER={HOST},{PORT};'
    f'DATABASE={DATABASE};'
    f'UID={USERNAME};'
    f'PWD={PASSWORD};'
    'Encrypt=no'  # Disable encryption for development
)

engine = create_engine(f'mssql+pyodbc:///?odbc_connect={params}')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()