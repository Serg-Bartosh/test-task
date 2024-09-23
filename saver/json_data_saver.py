import json
from typing import List, Dict

from dto.product_dto import ProductDto


class JSONDataSaver:
    def __init__(self, file_name: str) -> None:
        self.file_path: str = file_name
        self.structured_data: List[Dict[str, str]] = []

    def create_structured_data(self, data: List[ProductDto]) -> bool:
        if not data:
            return False
        for item in data:
            self.structured_data.append(item.to_dict())
        return True

    def create_file(self) -> None:
        if '.json' not in self.file_path:
            self.file_path += ".json"
        try:
            with open(self.file_path, 'w', encoding='utf-8') as json_file:
                json.dump(self.structured_data, json_file, ensure_ascii=False, indent=4)
            print(f"Data successfully saved to {self.file_path}")
        except Exception as e:
            print(f"Failed to save data: {e}")
