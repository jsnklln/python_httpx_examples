import httpx
import asyncio
import time

# this code is borrowed from https://www.twilio.com/blog/asynchronous-http-requests-in-python-with-httpx-and-asyncio

base_url = "https://pokeapi.co/api/v2/pokemon/"

def poke_sync():
    start_time = time.time()

    client = httpx.Client()

    for number in range(1, 151):
        resp = client.get(f"{base_url}{number}")
        pokemon = resp.json()
        print(pokemon['name'])

    return time.time() - start_time

def time_func(func, isasync=False):
    start_time = time.time()
    print("START")
    if isasync:
        asyncio.run(func())
    else:
        func()
    print("DONE")
    diff = time.time() - start_time
    return f"{func.__name__} took {diff}"

results = []
results.append(time_func(poke_sync))

print('\n'.join(results))
