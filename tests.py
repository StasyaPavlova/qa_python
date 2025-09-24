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

    def test_set_book_genre_positive(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        assert collector.get_book_genre('Властелин колец') == 'Фантастика'

    def test_set_book_genre_negative(self):
        collector = BooksCollector()
        collector.add_new_book('Поэзия')
        collector.set_book_genre('Поэзия', 'Недоступный жанр')
        assert collector.get_book_genre('Поэзия') == ''

    def test_get_book_genre_positive(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'
    
    def test_get_books_genre_positive(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.add_new_book('Король Лев')
        books_dict = collector.get_books_genre()
        assert 'Властелин колец' in books_dict
        assert 'Король Лев' in books_dict
        assert len(books_dict) == 2

    def test_get_books_with_specific_genre_positive(self):
        collector = BooksCollector()
        collector.add_new_book('Чужой')
        collector.set_book_genre('Чужой', 'Ужасы')
        assert collector.get_books_with_specific_genre('Ужасы') == ['Чужой']

    def test_get_books_with_specific_genre_negative(self):
        collector = BooksCollector()
        collector.add_new_book('Чужой')
        collector.set_book_genre('Чужой', 'Ужасы')
        assert collector.get_books_with_specific_genre('Комедии') == []

    def test_get_books_for_children(self):
        collector = BooksCollector()
        books = ['Властелин колец', 'Король Лев', 'Чужой', 'Сон в летнюю ночь', 'Молчание ягнят']
        genres = ['Фантастика', 'Мультфильмы', 'Ужасы', 'Комедии', 'Детективы']
        for i in range(5):
            collector.add_new_book(books[i])
            collector.set_book_genre(books[i], genres[i])
        books_for_children = collector.get_books_for_children()
        assert books_for_children == ['Властелин колец', 'Король Лев', 'Сон в летнюю ночь']

    def test_add_book_in_favorites_positive(self):
        collector = BooksCollector()
        book = 'Хоббит'
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        assert collector.get_list_of_favorites_books() == [book]

    def test_add_book_in_favorites_negative_not_in_books(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Властелин колец')
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_positive(self):
        collector = BooksCollector()
        book = 'Властелин колец'
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        collector.delete_book_from_favorites(book)
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_negative_not_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Хоббит')
        collector.add_book_in_favorites('Хоббит')
        collector.delete_book_from_favorites('Властелин колец')
        assert collector.get_list_of_favorites_books() == ['Хоббит']

    def test_get_list_of_favorites_books_only(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.add_new_book('Хоббит')
        collector.add_book_in_favorites('Хоббит')
        assert collector.get_list_of_favorites_books() == ['Хоббит']
        