back_front endpoints:
Админ панель https://roywest2.pythonanywhere.com/admin
Получения списка новостей по методу GET --> https://roywest2.pythonanywhere.com/news
Получения деталей новости (detail) по методу GET --> https://roywest2.pythonanywhere.com/news-detail/2 #id
Новости Создание новости (create) по методу POST --> https://roywest2.pythonanywhere.com/news-create/
Обновление новости (update) по методу POST --> https://roywest2.pythonanywhere.com/news-update/2 #id
Новости Удаление новости (delete) по методу POST --> https://roywest2.pythonanywhere.com/news-delete/2 #id
Новости Пример json строки для создания задания { "id": 1, "title": "1", "description": "1", "date": "2022-10-14T12:59:09.186457Z", "published": false }
И так далее по всем вашим endpoints
