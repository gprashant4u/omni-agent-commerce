from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from main import commerce_crew

app = FastAPI(title="OmniAgent Commerce API")

class UserQuery(BaseModel):
    user_input: str
    session_id: str

@app.post("/chat")
async def chat_endpoint(query: UserQuery):
    try:
        # Orchestrating multi-agent collaboration (Planner/Executor)
        # Satisfies: Multi-agent orchestration & session mgmt.
        result = commerce_crew.kickoff(inputs={
            'user_input': query.user_input,
            'session_id': query.session_id
        })
        return {"response": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
