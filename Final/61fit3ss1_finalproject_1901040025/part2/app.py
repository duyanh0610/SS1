
from flask import Flask, render_template, request, redirect, url_for
# from werkzeug.utils import redirect;
import sqlite3


app = Flask(__name__)
# create sql table
conn = sqlite3.connect('todolist.db') 
cs = conn.cursor()
cs.execute('CREATE TABLE IF NOT EXISTS todolist (id INTEGER PRIMARY KEY AUTOINCREMENT, description TEXT NOT NULL, status TEXT NOT NULL)') 
conn.commit()  
conn.close()




# routes
@app.route('/')
def homepage():
    conn = sqlite3.connect('todolist.db')
    cs = conn.cursor()
    cs.execute('SELECT * FROM todolist')
    
    todolist = [ dict(line) for line in [zip([ column[0] for column in cs.description], row) for row in cs.fetchall()] ]
    conn.commit()
    conn.close()
    return render_template ('home.html',  todoList =todolist)


@app.route('/add', methods=['POST']) 
def addItem(): 
    new_description = request.values['itemDescription']  
    
    conn = sqlite3.connect('todolist.db')
    cs = conn.cursor()
    cs.execute('SELECT * FROM todolist')
    todolist = cs.fetchall()
 
    
    cs.execute ('INSERT INTO todolist(description, status) VALUES(?,?)', ( new_description, 'Doing'))
    conn.commit()
    conn.close()


    return redirect(url_for('homepage'))


@app.route('/edit', methods =['POST','GET'])
def editItem(): 
    action = request.values['clickBtn']
    item_ID = int(request.values['itemID'])
    item_description = request.values['itemDescription']
    
    conn = sqlite3.connect('todolist.db')
    cs = conn.cursor()
    

    if action == 'delete':  
        cs.execute('DELETE FROM todolist WHERE id =:id', {'id': item_ID})  
        conn.commit()
        conn.close()


    if action == 'update':
        item_status = request.form.get('itemStatus')
        cs.execute('UPDATE todolist SET description = :description WHERE id = :id', {'description' : item_description , 'id': item_ID })
        if item_status == "Doing":
            cs.execute('UPDATE todolist SET status = :status WHERE id = :id', {'status': 'Done', 'id': item_ID})
        conn.commit()
        conn.close()

    return redirect(url_for('homepage'))


app.run(port= 3000,debug =True)
