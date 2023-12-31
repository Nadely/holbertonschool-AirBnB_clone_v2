#!/usr/bin/python3
"""
TestDBStorageDocs and TestDBStorage classes
and filestorage
"""
from datetime import datetime
import inspect
import models
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pycodestyle
import unittest
DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}
storage_t = os.getenv("HBNB_TYPE_STORAGE")


class TestDBStorage(unittest.TestCase):
    def setUp(self):
        """Initializes an instance of DBStorage"""
        self.db_storage = DBStorage()

    def tearDown(self):
        """Closes the DBStorage session"""
        self.db_storage.close()

    def test_initialization(self):
        """Test DBStorage initialization"""
        self.assertIsNotNone(self.db_storage._DBStorage__engine)
        self.assertIsNotNone(self.db_storage._DBStorage__session)

    def test_all_empty_database(self):
        """Test all() returns an empty dictionary for an empty database"""
        all_objects = self.db_storage.all()
        self.assertEqual(len(all_objects), 0)

    def test_all_objects_added(self):
        """Test all() returns all objects of a specific class"""
        user = User()
        self.db_storage.new(user)
        self.db_storage.save()
        all_users = self.db_storage.all(User)
        self.assertIn('User.{}'.format(user.id), all_users)

    def test_new(self):
        """Test new() adds a new object to the session"""
        state = State()
        self.db_storage.new(state)
        self.assertIn(state, self.db_storage._DBStorage__session.new)

    def test_reload(self):
        """Test reload() recreates the session and tables"""
        state = State(name="California")
        self.db_storage.new(state)
        self.db_storage.save()
        self.db_storage.reload()
        all_states = self.db_storage.all(State)
        self.assertEqual(len(all_states), 0)

    def test_close(self):
        """Test close() method"""
        self.db_storage.close()
        with self.assertRaises(Exception):
            self.db_storage.all()


class TestFileStorage(unittest.TestCase):
    """filestorage class"""
    @unittest.skipIf(storage_t != 'db', "not testing db storage")
    def test_all_returns_dict(self):
        """Test that all returns a dictionaty"""
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(storage_t != 'db', "not testing db storage")
    def test_all_no_class(self):
        """Test that all returns all rows when no class is passed"""

    @unittest.skipIf(storage_t != 'db', "not testing db storage")
    def test_new(self):
        """test that new adds an object to the database"""

    @unittest.skipIf(storage_t != 'db', "not testing db storage")
    def test_save(self):
        """Test that save properly saves objects to file.json"""

    class TestDBStorageDocs(unittest.TestCase):
        """Tests to check the documentation and style of DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8."""
        pep8s = pycodestyle.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Test tests/test_models/test_db_storage.py conforms to PEP8."""
        pep8s = pycodestyle.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == '__main__':
    unittest.main()
