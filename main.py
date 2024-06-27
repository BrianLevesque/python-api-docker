from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class Fact(BaseModel):
    id: int
    fact: str

facts = [Fact(id= 0, fact="""The planet's rotation is slowing down overall because of tidal forces between Earth and the moon. Roughly every 100 years, the day gets about 1.4 milliseconds, or 1.4 thousandths of a second, longer."""),
         Fact(id= 1, fact="Your brain is constantly eating itself. This process is called phagocytosis, "
                "where cells envelop and consume smaller cells or molecules to remove them from the system. Don’t worry! "
                "Phagocytosis isn't harmful, but actually helps preserve your grey matter."),
         Fact(id=2, fact="Animals can experience time differently from humans."),
         Fact(id=3, fact= "Water might not be wet."),
         Fact(id=4, fact="A chicken once lived for 18 months without a head."),
         Fact(id=5, fact="All the world’s bacteria stacked on top of each other would stretch for 10 billion light-years.")]


# Get method to get a random fact
@app.get("/fact")
async def main(id: int | None = None):
    if id:
        return facts[id]
    index = random.randint(0, len(facts)-1)
    return facts[index]

# Get method for specific fact


@app.get("/fact/{id}/")
async def main(id):
    return next((f for f in facts if f.id == int(id)), None)


# Post method for adding facts


@app.post("/fact/add_fact")
async def add(newFact: Fact):
    facts.append(newFact)
    return facts


