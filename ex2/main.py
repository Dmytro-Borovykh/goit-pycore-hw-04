def get_cats_info(path) -> list[dict]:
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cats_info = []
            for line in file:
                cat_id, name, age = line.split(',')
                cats_info.append(
                    {"id": cat_id.strip(), "name": name.strip(), "age": str(age.strip())})
            return cats_info
    except FileNotFoundError:
        print("Файл не знайдено.")
        return []
    except ValueError:
        print("Невірні дані у файлі.")
        return []


cats = get_cats_info('cats.txt')
print(cats)
