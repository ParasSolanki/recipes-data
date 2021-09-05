import json
import os

file = open("RecipesList.json", "r")

data = json.loads(file.read())

# os.chdir("new-recipes-with-cuisine")


def makeSlug(data):
    temp = (
        data.replace("-", "")
        .replace("|", "")
        .replace("&", "")
        .replace("/", "")
        .replace("(", "")
        .replace(")", "")
    ).split()
    return "-".join(temp).lower()


def formatIngredients(data):
    result = ""
    for item in data:
        result += "- " + item + ".\n"
    return result


def formatInstructions(data):
    result = ""
    for item in data:
        result += "1. " + item + ".\n"
    return result


def getCuisineSlug(cuisine):
    result = ""
    temp = cuisine.replace("\ufeff", "").split(" ")
    if type(temp) is list:
        result = "-".join(temp)
    elif type(temp) is str:
        result = temp
    return result.lower()


recipes = {"recipes": []}
recipeId = 1
for item in data["recipes"]:
    recipeName = item["recipeName"]
    slug = makeSlug(item["recipeName"])
    image = item["imageUrl"]
    prepTime = item["prepTime"]
    cuisine = item["cuisine"]
    cuisineSlug = getCuisineSlug(item["cuisine"])
    instructions = item["instructions"]
    ingredients = item["ingredients"]
    excerpt = (
        item["instructions"][0]
        .replace(":", "")
        .replace("'", "")
        .replace("|", "")
        .replace("&", "")
        .replace("/", "")
        .replace("(", "")
        .replace(")", "")
        .replace('''"''', "")
        .replace("^", "")
    )

    tempDict = {
        "id": recipeId,
        "name": recipeName,
        "slug": slug,
        "layout": "RecipeLayout",
        "prepTime": prepTime,
        "cuisine": cuisine,
        "cuisineSlug": cuisineSlug,
        "image": image,
        "excerpt": excerpt,
        "ingredients": ingredients,
        "instructions": instructions,
    }
    recipeId += 1
    recipes["recipes"].append(tempDict)

jsonFile = open("recipes.json", "w+")
jsonFile.write(json.dumps(recipes))
jsonFile.close()