import asyncio

"""
   asyncio.sleep() is an asynchronous function in Python's asyncio module.
   When you await asyncio.sleep(), it returns a coroutine that pauses the execution of the current coroutine (or task)
   for the specified duration without blocking the event loop. While the coroutine is sleeping,
   the event loop can continue processing other tasks.
"""


async def fetch_data(data: int) -> dict:
    print(f"Start fetching data...")
    await asyncio.sleep(data)
    return {"data": data}


async def custom_sleep(duration):
    for i in range(duration, 0, -1):
        print(f"Counter: {i}")
        await asyncio.sleep(1)  # Sleep for 1 second asynchronously


async def main():
    task = asyncio.create_task(fetch_data(5))
    await custom_sleep(2)
    # task.cancel()  # this will cancel the task and raise a CancelledError after some delay
    # print("5 seconds sleep complete and task.cancel() called: ", task.cancelled())
    # await custom_sleep(5)  # this will allow us to check if the task was cancelled
    # print("5 seconds sleep complete, task.cancelled(): ", task.cancelled())
    """
    task.result() retrieves the result of the task. If the task hasn't completed yet, 
    it will throw asyncio.exceptions.InvalidStateError: Result is not set.
    """
    try:
        data: dict = await asyncio.wait_for(task, timeout=5)
        print(data)  # We want this data within 5 seconds or else it is worthless to us and throw an exception

        # if task.done():
        #     data = task.result()
        #     print(data)
        # else:
        #     print("Task is not done yet!")
    except asyncio.CancelledError:
        print("Task was cancelled!")
    except asyncio.TimeoutError:
        print("Task took too long to complete!")


asyncio.run(main())
