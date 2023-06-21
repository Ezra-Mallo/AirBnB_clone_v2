#!/usr/bin/python3
"""New engine DBStorage: (models/engine/db_storage.py)"""
import os
import sqlalchemy
from sqlalchemy import create_engine, 

class DBStorage:
    """This it is the DBStorage class"""
    __engine = ""
    __session = ""

    classes = {
        'State': State,
        'City': City,
        'Place': Place,
        'Review': Review,
        'User': User,
        'Amenity': Amenity
    }

    def __init__(self):
        """Initialization"""
        user = os.environ.get(HBNB_MYSQL_USER)
        pswd = os.environ.get(HBNB_MYSQL_PWD)
        host = os.environ.get(HBNB_MYSQL_HOST)
        dbse: os.environ.get(HBNB_MYSQL_DB)
        env_var = os.environ.get(HBNB_ENV)

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                  format(user, pswd, host, dbse),
                                  pool_pre_ping=True)

        if env_var == "test":
            Base.metadata.delete_all()

    def all(self, cls=None):
        """This queries the current database session (self.__session)
        all objects depending of the class name (argument cls)"""
        my_dict = {}
        if cls is not None:
            my_query = self.__session.query(cls).all()
            for obj in my_query:
                key = "{}.{}".format(cls.__name__, obj.id)
                my_dict[key] = obj
        else:
            # to pick the specific item from the __classes
            for item_cls in self.__classes.values():
                for obj in self.__session.query(item_cls).all():
                    key = "{}.{}".format(item_cls.__name__, obj.id)
                    my_dict[key] = obj
        return my_dict

    def new(self, obj):
        """add the object to the current database session (self.__session)"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session (self.__session)"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database (feature of SQLAlchemy)
        (WARNING: all classes who inherit from Base must be imported before
        calling Base.metadata.create_all(engine))"""
        Base.metadata.create_all(self.__engine)
        new_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(new_session)
        self.__session = Session()
