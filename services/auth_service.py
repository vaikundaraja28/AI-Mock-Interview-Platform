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
                hashed
            )
        )

        conn.commit()

        return True

    except:

        return False

    finally:

        conn.close()


def login(email, password):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute(
        "SELECT password FROM users WHERE email=?",
        (email,)
    )

    row = cursor.fetchone()

    conn.close()

    if row is None:

        return False

    return bcrypt.checkpw(
        password.encode(),
        row[0]
    )