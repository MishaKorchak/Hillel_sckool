import os
import json

# Шлях до папки
folder_path = r"C:\Mikhail_study_Hillel_school_python\Mikhail_study_Hillel_school_python\Hillel_sckool\homework_json"

# Створення файлу для невалідних файлів
error_log_path = "resul_valid_json.log"  # Змініть your_second_name на своє прізвище
with open(error_log_path, "w", encoding="utf-8") as error_log:

    # Перевірка кожного файлу
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path) and file_name.endswith(".json"):
            try:

                with open(file_path, "r", encoding="utf-8") as file:
                    json.load(file)
            except (json.JSONDecodeError, IOError) as e:

                error_log.write(f"File {file_name} is not valid JSON. Error: {e}\n")

                print(f"File {file_name} is not valid JSON. Error: {e}")
