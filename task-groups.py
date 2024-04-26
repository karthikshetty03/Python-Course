import asyncio
from typing import Self


async def read_file(filename: str) -> str:
    with open(filename) as f:
        data: str = f.read()
    return data


async def fetch_data(data: int) -> dict:
    print("fetching data...")
    await asyncio.sleep(data)

    if data == 0:
        raise Exception("Data is zero")

    return {"data": data}


async def main():
    # tasks = asyncio.gather(
    #     fetch_data(1),
    #     fetch_data(2),
    #     fetch_data(0),
    #     return_exceptions=True
    # )
    #
    # values = await tasks
    # print(values)
    try:
        async with asyncio.TaskGroup() as tg:
            task1 = tg.create_task(fetch_data(1))
            task2 = tg.create_task(fetch_data(2))
            tg.create_task(read_file("whata-new.py"))
            tg.create_task(fetch_data(0))
        print("All tasks completed")
        print(task1.result())
        print(task2.result())
    except* Exception as eg:
        print(f"An error occurred: {eg.exceptions}")  # Exception for only 1 block after which it will get out


asyncio.run(main())

"""
return type pf Self
@classmethod is used to create a class method that returns an instance of the class.
"""
