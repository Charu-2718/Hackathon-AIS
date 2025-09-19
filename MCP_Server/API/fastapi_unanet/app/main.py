from fastapi import FastAPI

from app.controllers import contracts, expenses, people, projects, timesheets

app = FastAPI()

# Include routers
app.include_router(contracts.router)
app.include_router(expenses.router)
app.include_router(projects.router)
app.include_router(timesheets.router)
app.include_router(people.router) 
# url/docs

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", port = 5000, reload = True)