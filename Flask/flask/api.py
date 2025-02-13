"""
Put and Delete -HTTP Verbs
## Working with APIs JSON

"""
from flask import Flask,jsonify,request
app = Flask(__name__)
## Initial Data in the to do list
items= [
    {"id":1,'name':"Item1","Description":"This is item1"},
    {"id":2,'name':"Item2","Description":"This is item2"}


]
@app.route('/')
def home():
    return " Welcome to the sample ToDoList app"

@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)

## get: Retireve a specific item by id

@app.route('/items/<int:item_id>',methods=['GET'])
def get_item(item_id):
    item =next((item for item in items if item['id']==item_id),None)
    if item is None:
        return jsonify({"error":"item not found"})
    return jsonify(item)

@app.route('/items', methods =['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error":"item not found"})
    new_item={
        "id":items[-1]["id"]+1 if items else 1,
        "name": request.json['name'],
        "Description":request.json['Description']

    }
    items.append(new_item)
    return jsonify(new_item)

## Put: We update exisitng item
@app.route('/items/<int:item_id>', methods =['PUT'])
def update_item(item_id):
    item =next((item for item in items if item['id']==item_id),None)
    if item is None:
        return jsonify({"error":"item not found"})
    item['name'] = request.json.get('name',item['name'])
    item['Description'] = request.json.get('Description',item['Description'])
    return jsonify(item)
## Delete an item
@app.route('/items/<int:item_id>',methods=["DELETE"])
def delete_items(item_id):
    global items
    items =[item for  item in items if item['id'] != item_id]
    return jsonify({"result":"Item deleted"})

if __name__ == '__main__':
    app.run(debug=True)