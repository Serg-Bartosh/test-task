from typing import Optional


class ProductDto:
    def __init__(self, name: Optional[str] = None, description: Optional[str] = None, calories: Optional[str] = None,
                 carbs: Optional[str] = None, fats: Optional[str] = None, proteins: Optional[str] = None,
                 unsaturated: Optional[str] = None,
                 sugar: Optional[str] = None, salt_value: Optional[str] = None, portion: Optional[str] = None):
        self.name = name
        self.description = description
        self.calories = calories
        self.fats = fats
        self.carbs = carbs
        self.proteins = proteins
        self.unsaturated = unsaturated
        self.sugar = sugar
        self.salt = salt_value
        self.portion = portion

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "description": self.description,
            "calories": self.calories + " kcal" if self.calories else None,
            "fats": self.fats + "g" if self.fats else None,
            "carbohydrates": self.carbs + "g" if self.carbs else None,
            "proteins": self.proteins + "g" if self.proteins else None,
            "unsaturated_fats": self.unsaturated + "g" if self.unsaturated else None,
            "sugar": self.sugar + "g" if self.sugar else None,
            "salt": self.salt + "g" if self.salt else None,
            "portion": self.portion + "g" if self.portion else None
        }
