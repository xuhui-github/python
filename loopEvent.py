import asyncio

async def task():
    await asyncio.sleep(3)
    return 'task...'
coro= task()
#task1=asyncio.create_task(coro,name='task1')
loop =asyncio.get_event_loop()
result=loop.run_until_complete(coro)
print(result)
