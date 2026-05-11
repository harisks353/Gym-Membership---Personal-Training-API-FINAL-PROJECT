from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()
security = HTTPBasic()

# This is where I'll keep the member data since I'm not using a real DB yet
membership_registry = []

# Hardcoded logins for the staff - I used my ID for one of the passwords
GYM_STAFF = {
    "trainer_haris": "strong_pass_2026",
    "manager_70454": "fitness_goal_70454",
}

# --- Data Models ---

class TrainingSession(BaseModel):
    # Enforcing name length so people don't send empty or weirdly long strings
    activity_name: str = Field(..., min_length=3, max_length=50) 
    # Setting limits for session time so the math stays realistic
    duration_minutes: int = Field(..., ge=15, le=120)            
    hourly_rate: float = Field(..., ge=10.0)                     

class MemberRegistration(BaseModel):
    # I'm nesting the sessions list here to make the data more organized
    full_name: str
    membership_id: str
    chosen_sessions: List[TrainingSession] 
    has_premium_access: bool = False

# --- API Routes ---

@app.post("/register-membership")
def create_member_record(data: MemberRegistration):
    try:
        # Just summing up the rates to get the total cost for the user
        total_fees = sum(s.hourly_rate for s in data.chosen_sessions)
        
        # Save the registration to my global list
        membership_registry.append(data)
        
        return {
            "status": "Success",
            "total_to_pay": round(total_fees, 2),
            "data_received": data
        }
    except Exception:
        # Standard error response so the server doesn't just die with a 500 error
        raise HTTPException(status_code=400, detail="Something went wrong with the registration")

@app.get("/staff-portal/members")
def get_member_list(credentials: HTTPBasicCredentials = Depends(security)):
    # Checking if the username/password matches the STAFF_ACCESS dict
    authorized_pass = GYM_STAFF.get(credentials.username)
    
    if not authorized_pass or authorized_pass != credentials.password:
        # Throwing 401 if they aren't on the list
        raise HTTPException(status_code=401, detail="Invalid staff login")
    
    return membership_registry