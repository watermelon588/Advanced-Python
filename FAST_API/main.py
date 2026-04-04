from fastapi import FastAPI
import json
app = FastAPI()

# //helper functions
def get_data():
    with open('patients.json','r') as f:
        data = json.load(f)
    return data
@app.get("/")
def read_root():
    return {"Hello": "patient management system api"}
@app.get("/about")
def about():    
    return {"About": "A fully functional patient management system api built using FastAPI and SQLAlchemy."}   
@app.get("/view")
def view_patients():
    data = get_data()
    return data