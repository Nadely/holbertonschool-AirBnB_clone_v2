#!/usr/bin/python3
"""create New engine"""


from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import BaseModel, Base
from os import getenv


class DBStorage:
    """claas storage database"""
    __engine = None
    __session = None

    def __init__(self):
        """init method for dbstorage class"""
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)
        if env is not None and env == "test":
            Base.metadata.drop_all(self.__engine)

        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

    def all(self, cls=None):
        """Return a dictionary"""
        from models.state import State
        from models.city import City
        from models.user import User
        from models.place import Place
        from models.review import Review
        from models.amenity import Amenity
        from models.base_model import Base

        tables = {
            'users': User,
            'places': Place,
            'states': State,
            'cities': City,
            'amenities': Amenity,
            'reviews': Review
        }

        type_dict = {}

        if cls is None:
            for classes in tables.values():
                for row in self.__session.query(classes).all():
                    type_dict['{}.{}'
                                .format(classes.__name__, row.id)] = row
        else:
            for row in self.__session.query(cls):
                type_dict['{}.{}'.format(cls.__name__, row.id)] = row

        return type_dict

    def new(self, obj):
        """New method"""
        self.__session.add(obj)

    def save(self):
        """Save method"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete method"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload method"""
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """Close session method"""
        self.__session.close()
