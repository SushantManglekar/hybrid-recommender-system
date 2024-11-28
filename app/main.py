from fastapi import FastAPI

# Create FastAPI app instance
app = FastAPI()

# Root endpoint with a simple welcome message
@app.get("/")
def read_root():

    return {"message": "Welcome to the Hybrid Recommender System API!"}
