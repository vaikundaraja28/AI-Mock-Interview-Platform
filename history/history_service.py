import sqlite3

DATABASE = "database/interview.db"


def save_interview(
    user_id,
    role,
    difficulty,
    company,
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
            company,
            question,
            answer,
            evaluation,
            score
        )
        VALUES
        (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            user_id,
            role,
            difficulty,
            company,
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
            company,
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


def get_statistics(user_id):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            COUNT(*),
            AVG(score),
            MAX(score)
        FROM interviews
        WHERE user_id = ?
        """,
        (user_id,)
    )

    stats = cursor.fetchone()

    conn.close()

    return stats


def get_interview(interview_id):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            question,
            answer,
            evaluation
        FROM interviews
        WHERE id = ?
        """,
        (interview_id,)
    )

    interview = cursor.fetchone()

    conn.close()

    return interview

def get_scores(user_id):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            role,
            difficulty,
            score,
            question,
            company,
            created_at
        FROM interviews
        WHERE user_id = ?
        ORDER BY created_at
        """,
        (user_id,)
    )

    rows = cursor.fetchall()

    conn.close()

    return rows

def get_dashboard_data(user_id):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            role,
            difficulty,
            company,
            score,
            created_at
        FROM interviews
        WHERE user_id = ?
        """,
        (user_id,)
    )

    rows = cursor.fetchall()

    conn.close()

    return rows