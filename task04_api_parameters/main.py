# TO SET MULTIPLE PATH PARAMETERS AND QUERY PARAMETERS IN THE SAME ENDPOINT

from fastapi import FastAPI, Path, Query, Body, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float

# This is Enhanced Path Parameter: It's a part of the URL and it's Required Parameter - (Required):
@app.get("/items/{items_id}")
async def read_item(
    items_id: int = Path(
        ...,  # ... means the parameters is required
        title= "The ID of the item",
        description= "A unique identifier from the item",
        ge=1  # greater than or equal to 1
    )
):
    return {"items_id": items_id}

# This is Enhanced Query Parameter: (Query parameters are optional parameters that are passed in the URL after the ? mark)
@app.get("/items/")
async def read_item(
    q: str | None = Query(
        None, # Default value is None (optional parameter)
        title="Query string",
        description="Query string for searching items",
        min_length=3,
        max_length=50
        ),
    skip: int = Query(0, ge=0), # Greater than or equal to 0
    limit: int = Query(10, le=100)
):
    return {q: q, "skip": skip, "limit": limit}

# This is Multiple Parameters Together: (Path and Query parameters together)

@app.put("/items/validated/{item_id}")
async def update_item(
    item_id: int = Path(..., title="Item ID", ge=1),
    q: str | None = Query(None, min_length=3),
    item: Item | None = Body(None, description="Optional item data (JSON body)")
):
    result = {"item_id": item_id}
    if q:
        result.update({"q": q})
    if item:
        result.update({"item": item.model_dump()})
    return result