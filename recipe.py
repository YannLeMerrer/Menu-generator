class Recipe:
    def __init__(self, *, title: str, ingredients: list[str], steps: list[str], image: str):
        self.title = title
        self.ingredients = ingredients
        self.steps = steps
        self.image = image
