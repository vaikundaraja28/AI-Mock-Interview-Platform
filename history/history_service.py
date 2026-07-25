import sqlite3
import os


# =========================================================
# DATABASE PATH
# =========================================================

DATABASE = "database/interview.db"


# =========================================================
# DATABASE CONNECTION
# =========================================================

def get_connection():
    """
    Create and return a SQLite database connection.
    """

    # Make sure database directory exists
    os.makedirs(os.path.dirname(DATABASE), exist_ok=True)

    return sqlite3.connect(DATABASE)


# =========================================================
# SAVE INTERVIEW
# =========================================================

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
    """
    Save a completed interview into the database.
    """

    conn = get_connection()
    cursor = conn.cursor()

    try:

        # Convert score to float if possible
        try:
            score = float(score)
        except (TypeError, ValueError):
            score = 0.0

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

    except Exception as e:

        conn.rollback()

        print("Error saving interview:", e)

        raise e

    finally:

        conn.close()


# =========================================================
# GET INTERVIEW HISTORY
# =========================================================

def get_history(user_id):
    """
    Return interview history.

    Returned tuple structure:

    0 -> id
    1 -> role
    2 -> difficulty
    3 -> company
    4 -> score
    5 -> created_at
    """

    conn = get_connection()
    cursor = conn.cursor()

    try:

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

        return rows

    finally:

        conn.close()


# =========================================================
# GET SINGLE INTERVIEW
# =========================================================

def get_interview(interview_id):
    """
    Return details of one interview.

    Returns:

    question
    answer
    evaluation
    """

    conn = get_connection()
    cursor = conn.cursor()

    try:

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

        return interview

    finally:

        conn.close()


# =========================================================
# GET STATISTICS
# =========================================================

def get_statistics(user_id):
    """
    Return:

    total interviews
    average score
    highest score
    """

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute(
            """
            SELECT
                COUNT(*),
                COALESCE(AVG(score), 0),
                COALESCE(MAX(score), 0)
            FROM interviews
            WHERE user_id = ?
            """,
            (user_id,)
        )

        stats = cursor.fetchone()

        return stats

    finally:

        conn.close()


# =========================================================
# GET SCORES
# =========================================================

def get_scores(user_id):
    """
    Return interview scores for dashboard chart.

    Structure:

    0 -> role
    1 -> difficulty
    2 -> score
    3 -> question
    4 -> company
    5 -> created_at
    """

    conn = get_connection()
    cursor = conn.cursor()

    try:

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
            ORDER BY created_at ASC
            """,
            (user_id,)
        )

        rows = cursor.fetchall()

        return rows

    finally:

        conn.close()


# =========================================================
# GET DASHBOARD DATA
# =========================================================

def get_dashboard_data(user_id):
    """
    Return data required for dashboard analytics.

    Structure:

    0 -> role
    1 -> difficulty
    2 -> company
    3 -> score
    4 -> created_at
    """

    conn = get_connection()
    cursor = conn.cursor()

    try:

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
            ORDER BY created_at ASC
            """,
            (user_id,)
        )

        rows = cursor.fetchall()

        return rows

    finally:

        conn.close()