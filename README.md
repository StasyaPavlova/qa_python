# qa_python
Для проекта реализованы автотесты, которые покрывают основные методы класса:

- `test_add_new_book_add_two_books` — добавление двух книг.  
- `test_add_new_book_name_validation` — проверка ограничений длины и пустых названий.
- `test_set_book_genre_positive` — установка жанра корректной книги.  
- `test_set_book_genre_negative` — попытка установки недопустимого жанра.  
- `test_get_book_genre_positive` — получение жанра книги.  
- `test_get_books_genre_positive` — получение всего словаря книг.
- `test_get_books_with_specific_genre_positive` — книги с существующим жанром.  
- `test_get_books_with_specific_genre_negative` — проверка отсутствующего жанра.  
- `test_get_books_for_children` — получение книг, подходящих детям.
- `test_add_book_in_favorites_positive` — добавление книги в избранное.  
- `test_add_book_in_favorites_negative_not_in_books` — попытка добавить книгу, которой нет в словаре.  
- `test_delete_book_from_favorites_positive` — удаление книги из избранного.  
- `test_delete_book_from_favorites_negative_not_in_favorites` — попытка удалить книгу, которой нет в избранном.  
- `test_get_list_of_favorites_books_only` — получение списка избранных книг.


Запуск тестов производится командой:
pytest -v tests.py