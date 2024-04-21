import asyncio


# async keyword is used to define an asynchronous function
# this is also called a co-routine function: a function that can pause and resume its execution
# await keyword is used to pause the execution of the function until the awaited function is completed
# async function cannot be called directly, it must be awaited
# asyncio.run() is used to run the async function
# asyncio.sleep() is used to pause the execution of the async function for a given time
# asyncio.create_task() is used to create a task from a coroutine
async def main():
    # tasks are future objects that represent the result of a coroutine
    # tasks are non-blocking, meaning that the main function can continue to execute while the task is running
    # tasks can be awaited to get the result of the coroutine
    task1 = asyncio.create_task(fetch_data(10))
    task2 = asyncio.create_task(counter())
    data: dict = await task1
    print("Data:", data)
    await task2


async def fetch_data(data: int) -> dict:
    print("Start fetching data...")
    await asyncio.sleep(5)
    print("Data fetched successfully!")
    return {"data": data}


async def counter():
    for i in range(10):
        await asyncio.sleep(0.5)
        print("i", i)


# asyncio.run() function to run the main() function
asyncio.run(main())
