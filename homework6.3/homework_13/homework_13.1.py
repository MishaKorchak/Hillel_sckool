import csv

def remove_duplicates(file1, file2, output_file):
    unique_rows = set()  # Використовується для зберігання унікальних рядків

    # Читаємо дані з першого файлу
    with open(file1, mode='r', encoding='utf-8') as f1:
        reader = csv.reader(f1)
        for row in reader:
            unique_rows.add(tuple(row))  # Додаємо кожен рядок як кортеж у множину

    # Читаємо дані з другого файлу
    with open(file2, mode='r', encoding='utf-8') as f2:
        reader = csv.reader(f2)
        for row in reader:
            unique_rows.add(tuple(row))  # Додаємо рядки з другого файлу

    # Записуємо унікальні рядки у вихідний файл
    with open(output_file, 'w', encoding='utf-8', newline='') as f_out:
        writer = csv.writer(f_out)
        writer.writerows(sorted(unique_rows))  # Сортуємо перед записом (опціонально)

    print(f"Результат записано у файл: {output_file}")

if __name__ == "__main__":
    # Вкажіть шляхи до файлів
    file1_path = 'C:\Mikhail_study_Hillel_school_python\Mikhail_study_Hillel_school_python\Hillel_sckool\homework6.3\homework_13\random.csv'
    file2_path = 'C:\Mikhail_study_Hillel_school_python\Mikhail_study_Hillel_school_python\Hillel_sckool\homework6.3\homework_13\random-michaels.csv'
    output_file = 'C:\Mikhail_study_Hillel_school_python\Mikhail_study_Hillel_school_python\Hillel_sckool\homework6.3\homework_13\remove_duplicates.py..txt'



