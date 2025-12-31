import asyncio
from concurrent.futures import ProcessPoolExecutor


def encrypt(data):
    return f"lock {data[::-1]}"


async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, encrypt, "Credit_care_1234")
        print(result)


asyncio.run(main())
