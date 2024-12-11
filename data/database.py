import psycopg
from psycopg_pool import AsyncConnectionPool
from typing import Optional
import asyncio
import threading

# Connection URI and database configuration
POSTGRES_URI = "postgresql://postgres:admin@postgres:5432/data_analyzer"

class PostgresDB:
    _instance: Optional["PostgresDB"] = None
    _lock = threading.Lock()

    def __init__(self, uri: str = POSTGRES_URI):
        if PostgresDB._instance is not None:
            raise Exception("This class is a singleton. Use `get_instance()` to access the instance.")
        # Initialize the connection pool
        self.pool = AsyncConnectionPool(conninfo=uri)
        PostgresDB._instance = self

    @classmethod
    async def init(cls, uri: str = POSTGRES_URI):
        """
        Initialize the singleton instance.
        """
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:  # Double-checked locking
                    cls._instance = PostgresDB(uri)
        return cls._instance

    @classmethod
    async def get_instance(cls):
        """
        Retrieve the singleton instance.
        """
        if cls._instance is None:
            raise Exception("Instance not initialized. Call `init()` before using `get_instance()`.")
        return cls._instance

    async def get_connection(self):
        """
        Get a connection from the connection pool.
        """
        await self.pool.open()
        return await self.pool.getconn()

    async def release_connection(self, conn):
        """
        Release a connection back to the pool.
        """
        await self.pool.putconn(conn)

    async def close(self):
        """
        Close the connection pool and cleanup resources.
        """
        await self.pool.close()
        PostgresDB._instance = None  # Reset the singleton instance

# Example Usage
async def main():
    # Initialize the singleton instance
    await PostgresDB.init()

    # Get the singleton instance
    db = await PostgresDB.get_instance()

    # Get a connection from the pool
    conn = await db.get_connection()
    try:
        # Perform a query
        async with conn.cursor() as cur:
            await cur.execute("SELECT 1;")
            result = await cur.fetchone()
            print(result)
    finally:
        # Release the connection back to the pool
        await db.release_connection(conn)

    # Close the connection pool when done
    await db.close()

# Run the example
asyncio.run(main())
