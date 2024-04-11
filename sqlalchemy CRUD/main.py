from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, text
from sqlalchemy.sql.expression import update, delete

engine = create_engine("sqlite:///sample.db", echo=True)
print("ENGINE", engine)
print("TYPE OF ENGINE", type(engine))

meta= MetaData()

# There are 2 ways to create tables 
# 1. using declarative_base class 
# 2. Table class 
workers = Table(
    'workers',
    meta,
    Column('id', Integer,primary_key = True),
    Column('name', String)
)


# Below line is used to create the table in the database 
# Once the database and table is created we donot need this line so I have commented it out 
# meta.create_all(engine)


# *Inserting into Database
def insert(value):
    ins = workers.insert().values(name=value)
    print("INSTANCE TO INSERT: ", ins)
    print("Type OF INSTANCE TO INSERT: ", type(ins))
    conn = engine.connect()
    print("CONNECTION: ", conn)
    result = conn.execute(ins)
    print("RESULT: ", result)
    print("TYPE OF RESULT: ", result)
    return f"{value} inserted successfully"




# * UPDATE
def update_fun(existing_value,updating_value):
    conn = engine.connect()
    stmt = update(workers).where(workers.c.name==existing_value).values(name=updating_value)
    print("STATEMENT IS: ",stmt)
    update_result = conn.execute(stmt)
    print(update_result)
    wk = workers.select()
    print("WK IS: ", wk)
    result = conn.execute(wk).fetchall()
    print("RESULT IS: ", result)
    return f"{updating_value} updated successfully"




# * SELECT QUERY
def select():
    stmt = workers.select()
    conn = engine.connect()
    result = conn.execute(stmt)

    print("RESULT IS: ", result )
    for i in result: 
        print(i)


# * DELETE  QUERY: 
def delete(value):
    stmt = delete().where(workers.c.name==value)
    conn = engine.connect()
    conn.execute(stmt)
    allstmt = workers.select()
    print(conn.execute(allstmt).fetchall())
    return f"{value} deleted successfully"
 




# * Writing RAW Query
def raw_select():
    stmt = text("SELECT * FROM workers")
    conn = engine.connect()
    result = conn.execute(stmt).fetchall()
    print(result)
