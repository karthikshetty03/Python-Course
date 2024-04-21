import asyncio


async def counter():
    for i in range(10 ** 10):
        print(i)
        if i % 10000 == 0:
            await asyncio.sleep(0.01)


# It is not guaranteed that asyncio will execute the tasks,
# it has to get the opportunity to run the tasks
async def main():
    task = asyncio.create_task(counter())
    await asyncio.sleep(2)
    task.cancel()
    print('Task cancelled')
    await task  # This will raise a CancelledError exception


if __name__ == '__main__':
    asyncio.run(main())
