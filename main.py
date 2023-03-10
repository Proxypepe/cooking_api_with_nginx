import json

from fastapi import FastAPI, HTTPException
from mongoengine import connect, disconnect
import src.schemas.recipe as schemas
import src.models.recipe as models
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Recipe API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    connect(host='mongodb://admin:admin@mob-mongo:27017/cooking_recipe?authSource=admin')


@app.on_event("shutdown")
def shutdown_event():
    disconnect()


@app.get('/api/v1/recipes', status_code=200, response_model=list[schemas.Recipe])
async def get_recipes() -> list[schemas.Recipe]:
    recipes: list[models.Recipe] = models.Recipe.objects.all()
    result: list[Recipe] = []
    for recipe in recipes:
        tmp: dict = json.loads(
            recipe.to_json()
        )
        tmp['ingredients'] = len(tmp['ingredients'])
        tmp['steps'] = len(tmp['steps'])
        tmp.pop('description')
        result.append(schemas.Recipe(**tmp))
    return result


@app.get('/api/v1/recipes/{recipe_name}', status_code=200, response_model=schemas.FullRecipe)
async def get_recipe_by_name(recipe_name: str) -> schemas.FullRecipe:
    result: list[models.Recipe] = models.Recipe.objects(name=recipe_name)
    if not result:
        raise HTTPException(status_code=404)
    return schemas.FullRecipe(**json.loads(result[0].to_json()))


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', port=8080, log_level="debug", reload=True)
