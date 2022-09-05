from pydantic import BaseModel
import src.models.recipe as models


class RecipeBase(BaseModel):
    name: str
    prepare: str
    cook: str
    file_name: str
    tags: list[str]


class Recipe(RecipeBase):
    ingredients: int
    steps: int


class FullRecipe(RecipeBase):
    description: str
    ingredients: list[str]
    steps: list[str]


