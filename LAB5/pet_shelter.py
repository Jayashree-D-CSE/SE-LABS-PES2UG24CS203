"""Manage a simple animal shelter adoption register."""

import secrets
import sqlite3


def create_connection():
    """Create an in-memory SQLite database and its pets table."""
    connection = sqlite3.connect(":memory:")
    connection.execute(
        """
        CREATE TABLE pets (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            species TEXT NOT NULL,
            age INTEGER NOT NULL,
            adopted INTEGER NOT NULL DEFAULT 0
        )
        """
    )
    return connection


def register_pet(connection, name, species, age, tags=None):
    """Register a pet and return its tags."""
    if tags is None:
        tags = []

    connection.execute(
        """
        INSERT INTO pets (name, species, age, adopted)
        VALUES (?, ?, ?, 0)
        """,
        (name, species, age),
    )

    tags.append(species)
    return tags


def adopt(connection, pet_id, adoption_count):
    """Mark an available pet as adopted and update the count."""
    cursor = connection.execute(
        "UPDATE pets SET adopted = 1 WHERE id = ? AND adopted = 0",
        (pet_id,),
    )

    if cursor.rowcount > 0:
        adoption_count += 1

    return adoption_count


def adoption_code():
    """Generate a four-digit adoption code."""
    return f"PET-{secrets.randbelow(9000) + 1000}"


def oldest_available(connection):
    """Return the oldest available pet's name, or None if unavailable."""
    try:
        row = connection.execute(
            """
            SELECT name
            FROM pets
            WHERE adopted = 0
            ORDER BY age DESC
            LIMIT 1
            """
        ).fetchone()
    except sqlite3.Error:
        return None

    return row[0] if row is not None else None


def clear_unadopted(connection):
    """Delete pets that have not been adopted."""
    try:
        connection.execute("DELETE FROM pets WHERE adopted = 0")
    except sqlite3.Error as error:
        print(f"Could not clear unadopted pets: {error}")


def shelter_status(adoption_count):
    """Return the shelter's current activity status."""
    if adoption_count > 0:
        return "active"

    return "quiet"


def main():
    """Run a demonstration of the shelter adoption register."""
    connection = create_connection()
    adoption_count = 0

    register_pet(connection, "Bruno", "dog", 7)
    register_pet(connection, "Mitzi", "cat", 3)
    register_pet(connection, "Kiwi", "parrot", 12)

    adoption_count = adopt(connection, 1, adoption_count)

    print(
        oldest_available(connection),
        adoption_code(),
        shelter_status(adoption_count),
    )

    clear_unadopted(connection)
    connection.close()


if __name__ == "__main__":
    main()
