import sqlite3
import unittest
import test
from SI507project_tools import *
class FinalProjectSQLiteDBTests(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect(
            "sample_books.db")
        self.cur = self.conn.cursor()

    def test_for_countries_table(self):
        self.cur.execute(
            "select name, description, rating, type_id from books where id =1")
        data = self.cur.fetchone()
        self.assertEqual(data, ('<<How to play with cats?>>', 'no description!', 0.0, 1),
                         "Testing data that results from selecting book.id=1")


    def test_for_comments_table(self):
        res = self.cur.execute("select * from comments")
        data = res.fetchall()
        self.assertTrue(data, 'Testing that you get a result from making a query to the comments table')

    def test_for_types_table(self):
        self.cur.execute(
            "select name from types where id =1")
        data = self.cur.fetchone()
        self.assertEqual(data, ('Pets',),
                         "Testing data that results from selecting types.id=1")



    def test_book_insert_works(self):
        type = ("Cooking",)
        self.cur.execute(
            "insert into types(name) values (?)", type)
        self.conn.commit()

        self.cur.execute(
            "select name from types where name = 'Cooking'")
        data = self.cur.fetchone()
        self.assertEqual(data, type, "Testing a select statement where typeName = Cooking")

    def test_type_insert_works(self):
        book = ('The Mister',
                'The passionate new romance from E L James, author of the phenomenal #1 bestselling Fifty Shades Trilogy',
                8.8)
        self.cur.execute(
            "insert into books(name, description, rating) values (?, ?, ?)", book)
        self.conn.commit()

        self.cur.execute(
            "select name, description, rating from books where name = 'The Mister'")
        data = self.cur.fetchone()
        self.assertEqual(data, book, "Testing a select statement where bookName = The Mister")

    def test_foreign_key_book(self):
        res = self.cur.execute(
            "select * from books INNER JOIN types ON books.type_id = types.id")
        data = res.fetchall()
        self.assertTrue(data,
                        "Testing that result of selecting based on relationship between books and types does work")
        self.assertTrue(len(data) in [1, 2],
                        "Testing that there is in fact the amount of data entered that there should have been -- based on this query of everything in both tables.{}".format(
                            len(data)))


    def tearDown(self):
        self.conn.commit()
        self.conn.close()



class classTest(unittest.TestCase):

    def setUp(self):
        self.rating = Rating(1)

    def test_subclasses_instance_of_rating(self):
        self.assertIsInstance(self.rating, Rating,
                              "Testing that an instance of Rating is an instance of a subclass of Rating")

    def test_rating_str(self):
        rating = Rating(9)
        self.assertEqual(rating.value.__str__(), "9", "Testing string method on rating class")






if __name__ == '__main__':
    unittest.main(verbosity=2)