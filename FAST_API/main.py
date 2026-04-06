from fastapi import FastAPI , HTTPException , Path , Query
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
@app.get("/view/{patient_id}")
def view_patient(patient_id: str = Path(..., description="The ID of the patient to retrieve", example="P007")):
    data = get_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")
@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description="The field to sort by weight , height , bmi"), order: str = Query("asc", description="The order to sort by", example="asc" )):
    valid_sort_fields = ["weight", "height", "bmi"]
    if sort_by not in valid_sort_fields:
        raise HTTPException(status_code=400, detail=f"Invalid sort field. Valid options are: {', '.join(valid_sort_fields)}")
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid sort order. Valid options are: asc, desc") 
    data = get_data()

    sort_order = True if order == 'desc' else False

    sorted_data = sorted(data.values(),key=lambda x: x.get(sort_by,0), reverse=sort_order)
    return sorted_data
    