from flask import Flask, request, Response, json
from flask_cors import CORS
import sqlite3
import json

app = Flask(__name__)

CORS (app)


# create sql table
conn = sqlite3.connect('todolist.db') 
cs = conn.cursor()
cs.execute('CREATE TABLE IF NOT EXISTS todolist (id INTEGER PRIMARY KEY AUTOINCREMENT, description TEXT NOT NULL, status TEXT NOT NULL)') 
conn.commit()  
conn.close()

# list 
@app.route('/api/list', methods= ['GET'])
def list_item():
     #  connect to db and excecute
    conn =sqlite3.connect('todolist.db')
    cs= conn.cursor()
    cs.execute('SELECT * FROM todolist')

    todolist = [ dict(item) for item in [zip([ column[0] for column in cs.description], row) for row in cs.fetchall()] ]
    conn.commit()
    conn.close()

     # convert to json and return response
    return  Response(response= json.dumps(todolist))


# add
@app.route('/api/add', methods =['POST'])
def add_item(): 
    # get new description from request data
    req_data = request.get_json()

    new_description = req_data['itemDescription']
      
    #  connect to db and excecute
    conn = sqlite3.connect('todolist.db')
    cs = conn.cursor()
   
    cs.execute ('INSERT INTO todolist(description, status) VALUES( ?, ? )', (new_description, 'Doing'))
    conn.commit()
    conn.close()

    # convert to json and return response
    return Response (response = json.dumps(req_data))


# update
@app.route('/api/update', methods =['GET'])
def update_item():
    #  get id from route param
    item_id = request.args.get('id')

    #  connect to db and excecute
    conn = sqlite3.connect('todolist.db')
    cs = conn.cursor()
    cs.execute('SELECT * FROM todolist WHERE id= :id', {'id': item_id })
    item = cs.fetchone()
   
    if item[2] == 'Done':
        cs.execute('UPDATE todolist SET status = :status WHERE id = :id', {'status': 'Doing', 'id': item_id })
    if item[2] == 'Doing':
        cs.execute('UPDATE todolist SET status = :status WHERE id = :id', {'status': 'Done', 'id': item_id })
    
    todolist = [ dict(item) for item in [zip([ column[0] for column in cs.description], row) for row in cs.fetchall()]]
    conn.commit()
    conn.close()

    # convert to json and return response
    return Response(response=json.dumps(todolist))    

    
# delete
@app.route('/api/delete', methods =['GET'])
def delete_item(): 
    #  get id from route param
    item_id = request.args.get('id')
    
    #  connect to db and excecute
    conn = sqlite3.connect('todolist.db')
    cs = conn.cursor()
    cs.execute('DELETE FROM todolist WHERE id=:id', { 'id': item_id})

    cs.execute('SELECT * FROM todolist')
    todolist = [ dict(item) for item in [zip([ column[0] for column in cs.description], row) for row in cs.fetchall()] ]
    conn.commit()
    conn.close()

    # convert to json and return response
    return  Response(response= json.dumps(todolist))


app.run(port= 3000)
