from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


todoList = [
    {'id' : 1, 'description' : 'SS1 Assignment 1', 'status' : 'Done'},
    {'id' : 2, 'description' : 'SS1 Assignment 2', 'status' : 'Doing'},
    {'id' : 3, 'description' : 'SS1 Final', 'status' : 'Doing'}
]

# routes

@app.route('/')
def homepage():
    return render_template ('home.html',  todoList =todoList)

@app.route('/add', methods=['POST']) 
def addItem(): 
    new_description = request.values['itemDescription'] 

    item = {}
    item['id'] = len(todoList) + 1
    item['description'] =new_description
    item['status']= 'Doing'


    todoList.append(item)
    return redirect(url_for('homepage'))


@app.route('/edit', methods =['POST','GET'])
def editItem(): 
    action = request.values['clickBtn']
    item_ID = request.values['itemID']
    item_description = request.values['itemDescription']
    
  
    if action == 'delete':  
        
        todoList.pop(int(item_ID)-1)
        for item in todoList: 
            if(item['id'] > int(item_ID)): 
                item['id'] = item['id'] -1


    if action == 'update':
        item_status = request.form.get('itemStatus')
        
        for item in todoList: 
            if(item['id'] == int(item_ID)): 
                
                item['description'] = item_description
                if(item_status == "Doing"): 
                    item['status'] = "Done"
   


    return redirect(url_for('homepage'))




app.run(port= 3000,debug =True)