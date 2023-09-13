from flask import current_app
import sqlalchemy as sa
import pandas as pd

def connect_to_database():

    database_url = current_app.config['DATABASE_URL']
    database_user = current_app.config['DATABASE_USER']
    database_pass = current_app.config['DATABASE_PASSWD']
    database = current_app.config['DATABASE']
    
    connection_string = f'postgresql+psycopg2://{database_user}:{database_pass}@{database_url}/{database}'
    
    db_engine = sa.create_engine(connection_string)
    conn = db_engine.connect()

    return conn


def get_user_by_id(id: int):

    con = connect_to_database()

    query = f'''
        SELECT *
        FROM
            person
        WHERE
            id = '{id}'
    '''

    data = pd.read_sql(query, con=con)
    
    return data.iloc[0]


def get_user_by_email(email: str):


    con = connect_to_database()

    query = f'''
        SELECT *
        FROM
            person
        WHERE
            email = '{email}'
    '''

    data = pd.read_sql(query, con=con)
    
    return data.iloc[0]

def get_user_password(email: str):

    con = connect_to_database()

    query = f'''
        SELECT value
        FROM 
            person_password
        WHERE person_id  = (
            SELECT id
            FROM
                person
            WHERE
                email = '{email}'
        )
    '''

    data = pd.read_sql(query, con=con)

    if data.empty:
        return None

    first_row = data.iloc[0]

    return first_row['value']