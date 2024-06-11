import asyncio
async def numbers(numbers):
    for i in range(numbers):
        yield i
        await asyncio.sleep(0.5)
async def main():
    odd_numbers = [i async for i in numbers(10) if i % 2]
    print(odd_numbers)
if __name__ == '__main__':
    import time
    event_loop = asyncio.get_event_loop()
    try:
        s = time.perf_counter()
        event_loop.run_until_complete(main())
        print(time.perf_counter() - s)
    finally:
        event_loop.close()