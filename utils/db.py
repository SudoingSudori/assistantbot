"""
DB configuration

Reminders
    name            Name to be used in short view of the embed
    description     Description to be included into remind body
    start           When was added (in seconds Unix epoch, used also to calculate next repeat date)
    isrepeatable    True if the reminder is, obviously, repeatable
    repeatcount     Amount of repeats already done (to calculate next repeat)
    end             When to remind (in seconds)
"""

import aiosqlite
from typing import Optional

async def db_init(db: aiosqlite.Connection):
    await db.execute("CREATE TABLE IF NOT EXISTS reminders(name TEXT, description TEXT, start INTEGER,"
                     " isrepeatable INTEGER, repeatcount INTEGER, end INTEGER);")
    await db.commit()
    return

async def add_reminder(db: aiosqlite.Connection, name: str, description: str, end: int, isrepeatable: Optional[bool]):
    """
    Adds a reminder.
    Notes: start is counted from the moment of the function executing, repeatcount is default to 1 and increased separately
    """

async def remove_reminder(db: aiosqlite.Connection, name: str):
    """
    Removes the reminder by name.
    """

async def update_reminder(db: aiosqlite.Connection, name: str, update_data: dict):
    """
    Updates the reminder data.
    Notes: Primarily just to update the repeat counter, but could be used for other uses (updating description etc).
    """