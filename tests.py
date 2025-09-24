import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2
        assert 'Гордость и предубеждение и зомби' in collector.get_books_genre()
        assert 'Что делать, если ваш кот хочет вас убить' in collector.get_books_genre()

    @pytest.mark.parametrize("name, expected", [
        ('Ромео и Джульетта', True),
        ('', False),
        ('МастерМастерМастерМастерМастерМастерМастер', False)
    ])
    def test_add_new_book_name_validation(self, name, expected):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert (name in collector.get_books_genre()) == expected

    @pytest.mark.parametrize("book_name, genre, expected_genre", [
        ('Властелин колец', 'Фантастика', 'Фантастика'),
        ('Поэзия', '', '')  
    ])
    def test_set_and_get_book_genre(self, book_name, genre, expected_genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == expected_genre

    @pytest.mark.parametrize("books, genres, genre_to_check, expected_books", [
        (['Властелин колец', 'Чужой', 'Король Лев'],
         ['Фантастика', 'Ужасы', 'Мультфильмы'],
         'Ужасы',
         ['Чужой']),
        (['Властелин колец', 'Чужой', 'Король Лев'],
         ['Фантастика', 'Ужасы', 'Мультфильмы'],
         'Комедии',
         [])
    ])
    def test_get_books_with_specific_genre_only(self, books, genres, genre_to_check, expected_books):
        collector = BooksCollector()
        for i in range(len(books)):
            collector.add_new_book(books[i])
            collector.set_book_genre(books[i], genres[i])
        assert collector.get_books_with_specific_genre(genre_to_check) == expected_books

    @pytest.mark.parametrize("books, genres, favorites, expected_favorites", [
        (['Властелин колец', 'Хоббит'],
         ['Фантастика', 'Фантастика'],
         ['Хоббит'],
         ['Хоббит']),
        (['Властелин колец', 'Хоббит'],
         ['Фантастика', 'Фантастика'],
         [],
         [])
    ])
    def test_get_list_of_favorites_books_only(self, books, genres, favorites, expected_favorites):
        collector = BooksCollector()
        for i in range(len(books)):
            collector.add_new_book(books[i])
            collector.set_book_genre(books[i], genres[i])
        for book in favorites:
            collector.add_book_in_favorites(book)
        assert collector.get_list_of_favorites_books() == expected_favorites

    def test_get_books_for_children(self):
        collector = BooksCollector()
        books = ['Властелин колец', 'Король Лев', 'Чужой', 'Сон в летнюю ночь', 'Молчание ягнят']
        genres = ['Фантастика', 'Мультфильмы', 'Ужасы', 'Комедии', 'Детективы']
        for i in range(5):
            collector.add_new_book(books[i])
            collector.set_book_genre(books[i], genres[i])
        books_for_children = collector.get_books_for_children()
        assert books_for_children == ['Властелин колец', 'Король Лев', 'Сон в летнюю ночь']

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        book = 'Хоббит'
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        assert collector.get_list_of_favorites_books() == [book]

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        book = 'Властелин колец'
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        collector.delete_book_from_favorites(book)
        assert collector.get_list_of_favorites_books() == []
