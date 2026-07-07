import sqlite3
import bcrypt

DATABASE = "database/interview.db"


def register(name, email, password):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    hashed = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    try:

        cursor.execute(
            """
            INSERT INTO users(name,email,password)
            VALUES(?,?,?)
            """,
            (
                name,
                email,
                hashed.decode()
            )
        )

        conn.commit()

        return True

    except sqlite3.IntegrityError:

        return False

    finally:

        conn.close()


def login(email, password):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id,name,password
        FROM users
        WHERE email=?
        """,
        (email,)
    )

    user = cursor.fetchone()

    conn.close()

    if user is None:
        return None

    if bcrypt.checkpw(
        password.encode(),
        user[2].encode()
    ):

        return {
            "id": user[0],
            "name": user[1],
            "email": email
        }

    return None