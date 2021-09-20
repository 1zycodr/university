import sqlite3


class Db:
    _connection = None
    _cursor = None

    @classmethod
    def init(cls):
        cls._connection = sqlite3.connect('db.sqlite3')
        cls._cursor = cls._connection.cursor()

        cls._cursor.execute("""CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(20) NOT NULL UNIQUE,
            salt VARCHAR(32) NOT NULL,
            password VARCHAR(32) NOT NULL,
            blocked BOOLEAN DEFAULT FALSE,
            count INT DEFAULT 0
        );""")

        cls._cursor.execute("SELECT * FROM users")
        print(cls._cursor.fetchall())

    @classmethod
    def execute(cls, query: str) -> tuple[list, str]:
        try:
            cls._cursor.execute(query)
            cls._connection.commit()
            return cls._cursor.fetchall(), None
        except Exception as ex:
            return None, str(ex)

    @classmethod
    def close(cls) -> tuple[bool, str]:
        try:
            cls._cursor.close()
            cls._connection.close()
            return True, None
        except Exception as ex:
            return False, str(ex)

    @classmethod
    def create_user(
        cls,
        username: str,
        salt: bytes,
        key: bytes
    ) -> tuple[bool, str]:
        try:
            query = "INSERT INTO users (username, salt, password)\
                VALUES (?,?,?)"
            cls._cursor.execute(query, (username, salt, key))
            cls._connection.commit()
            return True, None
        except Exception as ex:
            return False, str(ex)

    @classmethod
    def user_exists(cls, username: str) -> tuple[bool, str]:
        try:
            query = "SELECT * FROM users WHERE username=?"
            cls._cursor.execute(query, (username,))
            return bool(cls._cursor.fetchall()), None
        except Exception as ex:
            print(ex)
            return False, str(ex)

    @classmethod
    def get_user(cls, username: str) -> tuple[list, str]:
        try:
            query = "SELECT * FROM users WHERE username=?"
            cls._cursor.execute(query, (username,))
            return cls._cursor.fetchall(), None
        except Exception as ex:
            return None, str(ex)

    @classmethod
    def increment_count(cls, username: str) -> tuple[bool, str]:
        try:
            query = "SELECT count FROM users WHERE username=?"
            cls._cursor.execute(query, (username,))

            count = cls._cursor.fetchone()[-1]

            if count == 2:
                query = "UPDATE users SET count=?, blocked=TRUE \
                    WHERE username=?"
            else:
                query = "UPDATE users SET count=? WHERE username=?"

            cls._cursor.execute(query, (count + 1, username))
            cls._connection.commit()

            return True, None
        except Exception as ex:
            return False, str(ex)


if __name__ == '__main__':
    print('you should not run this module directly')
