# MongoDB setup
from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["todo_db"]
collection = db["items"]

# To-Do Page route
@app.route("/todo")
def todo():
    return render_template("todo.html")

# Backend route to handle form submission
@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    item_name = request.form.get("itemName")
    item_desc = request.form.get("itemDescription")
    
    if item_name and item_desc:
        collection.insert_one({"name": item_name, "description": item_desc})
    
    return redirect("/todo")
