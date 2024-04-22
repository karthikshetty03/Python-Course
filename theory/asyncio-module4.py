import asyncio


async def fetch_data(data: int) -> dict:
    print(f"Fetching data...")
    await asyncio.sleep(data)
    if data == 0:
        raise Exception("Data is invalid")
    return {"data": data}


async def main():
    tasks = [fetch_data(i) for i in range(0, 4)]
    """
    asyncio.gather() is used to run multiple tasks concurrently and await for all of them to complete.
    if we do not use return_exceptions=True, then the first exception raised by any of the tasks will be raised 
    and the rest of the tasks will be cancelled.
    """
    results = await asyncio.gather(*tasks, return_exceptions=True)
    print(results)


if __name__ == "__main__":
    asyncio.run(main())
