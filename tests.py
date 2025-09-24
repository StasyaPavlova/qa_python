import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_rating()) == 2

    @pytest.mark.parametrize("name,expected_count", [
        ("Гарри Поттер", 1),
        ("", 0),
        ("Мастер и Маргарита" * 5, 0)
    ])
    def test_add_new_book_name_validation(self, name, expected_count):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == expected_count  

    @pytest.mark.parametrize("genre,expected", [
        ("Фантастика", "Фантастика"),
        ("Поэзия", "")
    ])
    def test_set_and_get_book_genre(self, genre, expected):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", genre)
        assert collector.get_book_genre("Гарри Поттер") == expected  

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.add_new_book("Шерлок Холмс")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        collector.set_book_genre("Шерлок Холмс", "Детективы")

        books = collector.get_books_with_specific_genre("Фантастика")
        assert books == ["Гарри Поттер"]

    def test_get_books_genre_returns_dict(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")

        result = collector.get_books_genre()
        assert isinstance(result, dict)
        assert result == {"Гарри Поттер": "Фантастика"}

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.add_new_book("Шерлок Холмс")
        collector.set_book_genre("Гарри Поттер", "Фантастика")  
        collector.set_book_genre("Шерлок Холмс", "Детективы")   

        books_for_children = collector.get_books_for_children()
        assert "Гарри Поттер" in books_for_children
        assert "Шерлок Холмс" not in books_for_children

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Хоббит")
        collector.add_book_in_favorites("Хоббит")
        collector.add_book_in_favorites("Хоббит")  

        favorites = collector.get_list_of_favorites_books()
        assert favorites == ["Хоббит"]

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Хоббит")
        collector.add_book_in_favorites("Хоббит")
        collector.delete_book_from_favorites("Хоббит")

        favorites = collector.get_list_of_favorites_books()
        assert favorites == []

    @pytest.mark.parametrize("name", ["Властелин колец", "Король Лев"])
    def test_add_book_in_favorites_not_in_books_genre(self, name):
        collector = BooksCollector()
        collector.add_book_in_favorites(name)
        favorites = collector.get_list_of_favorites_books()
        assert favorites == []
