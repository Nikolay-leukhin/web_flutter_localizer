import pandas as pd
import json
import os


class Localizer:
    def __init__(self, csv_path: str, keyname_column: str):
        self.__csv_path = csv_path
        self.keyname_column = keyname_column
        self.df = pd.read_csv(csv_path)

    def load_arb_country_file(self, country_name: str, output_file_name: str):
        df = self.df[[self.keyname_column, country_name]]
        localization_data = df.set_index(self.keyname_column)[country_name].to_dict()
        with open(output_file_name, 'w', encoding='utf-8') as file:
            json.dump(localization_data, file, ensure_ascii=False, indent=2)

    def load_all_files(self, output_folder: str):
        all_localization_keys = self.df.columns.tolist()
        all_localization_keys.remove(self.keyname_column)
        generated_files = []

        for localize_name in all_localization_keys:
            output_file = os.path.join(output_folder, f"app_{localize_name}.arb")
            self.load_arb_country_file(localize_name, output_file)
            generated_files.append(f"app_{localize_name}.arb")

        return generated_files