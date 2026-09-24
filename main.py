import json
from fastapi import FastAPI, HTTPException
from models import patient, patient_update

app = FastAPI()

with open("patients.json" , "r")as file:

    patients = json.load(file)

# @app.get("/patients")
# def patients_data():
#     return patients

@app.get("/patients/{patient_id}")  #Path parameter
def get_patient(patient_id):
    for patient in patients:
        if patient["patient_id"]== patient_id:
            return patient

    raise HTTPException(
    status_code=404,
    detail="Patient not found"
)
    

# @app.get("/patients")                   #Query parameter
# def patients_data(gender: str = None): 

#     if gender is None:
#         return patients

#     filtered_patients=[]

#     for patient in patients:
#         if patient["gender"] == gender:
#             filtered_patients.append(patient)

#     return filtered_patients

@app.get("/patients")    #Multiple Queryy
def patients_data(gender: str =None , admitted: bool =None): 
    if gender is None and admitted is None:
         return patients

    filtered_patients= []

    for patient in patients:

          if (
            (gender is None or patient["gender"] == gender)
            and
            (admitted is None or patient["admitted"] == admitted)
        ):
            filtered_patients.append(patient)

    return filtered_patients


@app.post("/patients")                                                   #VALIDATION AND DUPLICATES
def create_patient(patient: patient):
    patient_data = patient.model_dump()

    for patient in patients:
        if patient["patient_id"] == patient_data["patient_id"]:
            raise HTTPException(
                status_code=409,
                detail="Patient ID already exists"
            )

    patients.append(patient_data)
    return patient_data


@app.put("/patients/{patient_id}")
def update_patient(patient_id: str, patient: patient):

    patient_data = patient.model_dump()

    for existing_patient in patients:
        if existing_patient["patient_id"] == patient_id:
            existing_patient.update(patient_data)                            #python build-in function
            return existing_patient

    raise HTTPException(
        status_code=404,
        detail="Patient not found"
    )

@app.patch("/patients/{patient_id}")
def update_patient_partial(patient_id: str, patient: patient_update):

    patient_data = patient.model_dump(exclude_unset=True)

    for p in patients:
        if p["patient_id"] == patient_id:

            p.update(patient_data)

            return p

    raise HTTPException(
        status_code=404,
        detail="Patient not found"
    )

@app.delete("/patients/{patient_id}")
def delete_patient(patient_id: str):

    for p in patients:
        if p["patient_id"] == patient_id:
            patients.remove(p)
            return {
                "message": "Patient deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Patient not found"
    )