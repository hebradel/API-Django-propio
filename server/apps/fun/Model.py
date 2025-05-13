# apps.fun.Model.py
import sqlite3

class Field:
    def __init__(self, max_length=None, primary_key=False, null=False, blank=False):
        self.max_length = max_length
        self.primary_key = primary_key
        self.null = null
        self.blank = blank

class AutoField(Field):
    pass

class CharField(Field):
    pass

class ModelMeta(type):
    def __new__(cls, name, bases, attrs):
        fields = {key: value for key, value in attrs.items() if isinstance(value, Field)}
        attrs['_fields'] = fields
        return super().__new__(cls, name, bases, attrs)

class Model(metaclass=ModelMeta):
    def __init__(self, **kwargs):
        for field in self._fields:
            value = kwargs.get(field)
            setattr(self, field, value)

    def save(self):
        fields = ', '.join(self._fields.keys())
        values = tuple(getattr(self, field) for field in self._fields)
        placeholders = ', '.join(['?' for _ in self._fields])

        if hasattr(self, 'id') and self.id:
            query = f"UPDATE {self.__class__.__name__.lower()} SET " + ", ".join([f"{field} = ?" for field in self._fields]) + " WHERE id = ?"
            self.execute_query(query, values + (self.id,))
        else:
            query = f"INSERT INTO {self.__class__.__name__.lower()} ({fields}) VALUES ({placeholders})"
            self.execute_query(query, values)
            self.id = self.get_last_inserted_id()

    def delete(self):
        if not hasattr(self, 'id') or not self.id:
            raise ValueError("Instance does not exist in the database.")
        query = f"DELETE FROM {self.__class__.__name__.lower()} WHERE id = ?"
        self.execute_query(query, (self.id,))

    @classmethod
    def create_table(cls):
        columns = []
        for field, field_type in cls._fields.items():
            column = f"{field} TEXT"
            if isinstance(field_type, AutoField):
                column = f"{field} INTEGER PRIMARY KEY AUTOINCREMENT"
            elif isinstance(field_type, CharField) and field_type.max_length:
                column = f"{field} TEXT({field_type.max_length})"
            columns.append(column)

        query = f"CREATE TABLE IF NOT EXISTS {cls.__name__.lower()} ({', '.join(columns)})"
        cls.execute_query(query)

    @classmethod
    def execute_query(cls, query, params=()):
        conn = sqlite3.connect('py.sqlite3')
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        conn.close()

    @classmethod
    def get_last_inserted_id(cls):
        conn = sqlite3.connect('py.sqlite3')
        cursor = conn.cursor()
        cursor.execute("SELECT last_insert_rowid()")
        last_id = cursor.fetchone()[0]
        conn.close()
        return last_id

    @classmethod
    def get(cls, **kwargs):
        conditions = ' AND '.join([f"{k} = ?" for k in kwargs.keys()])
        query = f"SELECT * FROM {cls.__name__.lower()} WHERE {conditions} LIMIT 1"
        
        conn = sqlite3.connect('py.sqlite3')
        cursor = conn.cursor()
        cursor.execute(query, tuple(kwargs.values()))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            values = {field: row[idx] for idx, field in enumerate(cls._fields.keys())}
            return cls(**values)
        
        return None  # Si no hay resultado, retornar None

    @classmethod
    def filter(cls, **kwargs):
        conditions = ' AND '.join([f"{k} = ?" for k in kwargs.keys()])
        query = f"SELECT * FROM {cls.__name__.lower()} WHERE {conditions}"
        conn = sqlite3.connect('py.sqlite3')
        cursor = conn.cursor()
        cursor.execute(query, tuple(kwargs.values()))
        rows = cursor.fetchall()
        conn.close()

        instances = []
        for row in rows:
            values = {field: row[idx] for idx, field in enumerate(cls._fields.keys())}
            instances.append(cls(**values))
        return instances

    @classmethod
    def all(cls):
        query = f"SELECT * FROM {cls.__name__.lower()}"
        conn = sqlite3.connect('py.sqlite3')
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()

        instances = []
        for row in rows:
            values = {field: row[idx] for idx, field in enumerate(cls._fields.keys())}
            instances.append(cls(**values))
        return instances