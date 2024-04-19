"""
DB configuration

Reminders
    name            Name to be used in short view of the embed
    description     Description to be included into remind body
    start           When was added (in seconds Unix epoch, used also to calculate next repeat date)
    isrepeatable    True if the reminder is, obviously, repeatable
    repeatcount     Amount of repeats already done (to calculate next repeat)
    end             When to remind (offset, in seconds)
"""

import aiosqlite
import asyncio
import time
from typing import Optional


class ReminderDB():

    def __init__(self, db: aiosqlite.Connection):
        self.db = db
    
    async def db_init(self):
        await self.db.execute("CREATE TABLE IF NOT EXISTS reminders(name TEXT, description TEXT, start INTEGER,"
                        " isrepeatable INTEGER, repeatcount INTEGER, end INTEGER);")
        await self.db.commit()

    async def add(self, name: str, description: str, end: int, isrepeatable: Optional[bool] = False):
        """
        Adds a reminder.
        Notes: start is counted from the moment of the function executing, repeatcount is default to 0 and increased separately
        """
        start = time.time()
        isrepeatable = int(isrepeatable)
        repeatcount = 0
        await self.db.execute("INSERT INTO reminders(name, description, start, isrepeatable, repeatcount, end) VALUES (?, ?, ?, ?, ?, ?);", 
                        (name, description, start, isrepeatable, repeatcount, end))
        await self.db.commit()
        return

    async def remove(self, name: str):
        """
        Removes the reminder by name.
        """
        await self.db.execute("DELETE FROM reminders WHERE name = ?;", (name,))
        await self.db.commit()
        return

    async def update(self, name: str, update_data: dict):
        """
        Updates the reminder data.
        Notes: Primarily just to update the repeat counter, but could be used for other uses (updating description etc).
        """