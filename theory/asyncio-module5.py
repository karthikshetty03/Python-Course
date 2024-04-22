import asyncio


async def counter(num: int):
    for i in range(num):
        print("i", i)
        if i % 10_000 == 0:
            await asyncio.sleep(0)


async def main():
    print("started!")
    task = asyncio.create_task(counter(100_000_000))
    """
    The asyncio.sleep() function is a coroutine that completes after a given time in seconds.
    value 0 does not slow down the program, but it gives an opportunity to other coroutines to run.
    """
    await asyncio.sleep(1)
    # result = await asyncio.sleep(0, result={"item": "123"})
    # print(result)
    task.cancel()

    """
    In this case, because the cancellation happens while the counter coroutine is not actively doing any 
    asynchronous operations (like I/O or waiting for another coroutine), it doesn't raise a CancelledError. Instead, 
    the cancellation cleanly stops the coroutine without raising an exception.

    So, in your case, since the cancellation happens during the execution of the coroutine and not while it's 
    blocking on an awaitable operation, it doesn't raise an exception. The program simply exits with exit code 0, 
    indicating successful execution.
    
    If you put the below block and await for the task, it will raise an exception.
    """
    # try:
    #     await task
    # except asyncio.CancelledError:
    #     print("task was cancelled")


if __name__ == "__main__":
    asyncio.run(main())
