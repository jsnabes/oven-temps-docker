import random
from fastapi import FastAPI
from pydantic import BaseModel, Field, computed_field
import uvicorn


# ASGI Server:
app = FastAPI()

class Oven(BaseModel):
    min: int = Field(ge=250, le=500)
    max: int = Field(ge=250, le=500)

    @computed_field
    @property
    def reading(self) -> int:
        return random.randint(self.min,self.max)

@app.get("/")
async def get_reading():
    return {'reading': o.reading}

if __name__ == '__main__':
    o = Oven(min=250, max="500")
    uvicorn.run(app, host='0.0.0.0', port=8000)






