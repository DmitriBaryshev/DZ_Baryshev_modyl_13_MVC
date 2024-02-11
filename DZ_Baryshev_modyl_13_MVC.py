# Задание 1
class Shoe:
    def __init__(self, shoe_type, shoe_style, color, price, manufacturer, size):
        self.shoe_type = shoe_type
        self.shoe_style = shoe_style
        self.color = color
        self.price = price
        self.manufacturer = manufacturer
        self.size = size


class ShoeController:
    def create_shoe(self, shoe_type, shoe_style, color, price, manufacturer, size):
        shoe = Shoe(shoe_type, shoe_style, color, price, manufacturer, size)
        return shoe


class ShoeView:
    def print_shoe_details(self, shoe):
        print("Shoe Type:", shoe.shoe_type)
        print("Shoe Style:", shoe.shoe_style)
        print("Color:", shoe.color)
        print("Price:", shoe.price)
        print("Manufacturer:", shoe.manufacturer)
        print("Size:", shoe.size)


controller = ShoeController()
shoe = controller.create_shoe("мужская", "кроссовки", "черный", 5000, "Nike", 44)

view = ShoeView()
view.print_shoe_details(shoe)


# Задание 2
class Recipe:
    def __init__(self, name, author, recipe_type, description, video_link, ingredients, cuisine):
        self.name = name
        self.author = author
        self.recipe_type = recipe_type
        self.description = description
        self.video_link = video_link
        self.ingredients = ingredients
        self.cuisine = cuisine


class RecipeController:
    def create_recipe(self, name, author, recipe_type, description, video_link, ingredients, cuisine):
        recipe = Recipe(name, author, recipe_type, description, video_link, ingredients, cuisine)
        return recipe


class RecipeView:
    def print_recipe_details(self, recipe):
        print("Recipe Name:", recipe.name)
        print("Author:", recipe.author)
        print("Recipe Type:", recipe.recipe_type)
        print("Description:", recipe.description)
        print("Video Link:", recipe.video_link)
        print("Ingredients:", recipe.ingredients)
        print("Cuisine:", recipe.cuisine)


controller = RecipeController()
recipe = controller.create_recipe("Spaghetti Carbonara", "Chef John", "Main Course", "Delicious spaghetti carbonara with eggs and pancetta.", "https://www.youtube.com/watch?v=PFQs0Xy9BvM", ["spaghetti", "eggs", "pancetta", "cheese"], "Italian")

view = RecipeView()
view.print_recipe_details(recipe)

