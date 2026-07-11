import sqlite3

DATABASE = "database/interview.db"


def save_interview(
    user_id,
    role,
    difficulty,
    question,
    answer,
    evaluation,
    score
):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO interviews
        (
            user_id,
            role,
            difficulty,
            question,
            answer,
            evaluation,
            score
        )
        VALUES
        (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            user_id,
            role,
            difficulty,
            question,
            answer,
            evaluation,
            score
        )
    )

    conn.commit()

    conn.close()


def get_history(user_id):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            id,
            role,
            difficulty,
            score,
            created_at
        FROM interviews
        WHERE user_id = ?
        ORDER BY created_at DESC
        """,
        (user_id,)
    )

    rows = cursor.fetchall()

    conn.close()

    return rows