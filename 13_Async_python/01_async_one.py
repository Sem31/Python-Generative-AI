# async: def declear a coroutine(special function that can be paused)

# await: pauses execution until the result is ready

# asyncion: Built in python library
# Event Loop: The engine that runs and schedules co-rountines in python.

# @ Reason asyncio and await does not block your main thread

import asyncio


async def brew_chai():
    print("Brewing chai...")
    await asyncio.sleep(2)
    print("Chai is ready!")


asyncio.run(brew_chai())
