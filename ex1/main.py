
def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total_salary = 0
            length = 0

            for line in file:
                _, salary = line.split(',')
                total_salary += int(salary.strip())
                length += 1

        if length == 0:
            return 0, 0

        average = int(total_salary / length)
        return total_salary, average

    except FileNotFoundError:
        print("Файл не знайдено.")
        return 0, 0

    except ValueError:
        print("Невірні дані у файлі.")
        return 0, 0


total, average = total_salary('salary.txt')
print(
    f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
