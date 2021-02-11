import os
import logging
import psycopg2
from pathlib import Path
from dotenv import find_dotenv, load_dotenv


def read_sql(filename):
    """
    Open and read the file as a single buffer
    :return:
    The string file in memory
    """
    fd = open(filename, 'r')
    sql_file = fd.read()
    fd.close()
    return sql_file

def init_connection():
    """
    Function that searches into a respective user's env folder
    to return connection objects for database
    :return:
    Cursor and Connection Objects
    """

    # Retrieve AWS .env variables
    aws_database = os.environ.get('aws_database')
    aws_host = os.environ.get('aws_host')
    aws_port = os.environ.get('aws_port')
    aws_user = os.environ.get('aws_user')
    aws_password = os.environ.get('aws_password')

    # Using the env variables, connect into the MDW
    conn = psycopg2.connect("dbname={} host={} port={} user={} password={}".format(aws_database,
                                                                                   aws_host,
                                                                                   aws_port,
                                                                                   aws_user,
                                                                                   aws_password))
    # Connection is successful and return the connection
    return conn


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    init_connection()
