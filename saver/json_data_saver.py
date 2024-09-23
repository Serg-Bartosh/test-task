import json

from lxml.objectify import BoolElement


class JSONDataSaver:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.structured_data = []

    def create_structured_data(self, data: [[str, ]]) -> BoolElement:
        if len(data) == 0:
            return False
        for item in data:
            product_data = {
                "name": item[0].lower(),
                "description": item[1].lower(),
                "calories": item[2].lower() + " kcal",
                "fats": item[3].lower() + "g",
                "carbohydrates": item[4].lower() + "g",
                "proteins": item[5].lower() + "g",
                "unsaturated_fats": item[6].lower() + "g",
                "sugar": item[7].lower() + "g",
                "salt": item[8].lower() + "g",
                "portion": item[9].lower() + "g"
            }
            self.structured_data.append(product_data)
        return True

    def create_file(self):
        if '.json' not in self.file_name:
            self.file_name += ".json"
        try:
            with open(self.file_name, 'w', encoding='utf-8') as json_file:
                json.dump(self.structured_data, json_file, ensure_ascii=False, indent=4)
            print(f"Data successfully saved to {self.file_name}")
        except Exception as e:
            print(f"Failed to save data: {e}")
