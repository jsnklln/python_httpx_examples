import httpx
import asyncio
import time

# this code is borrowed from https://www.twilio.com/blog/asynchronous-http-requests-in-python-with-httpx-and-asyncio

base_url = "https://pokeapi.co/api/v2/pokemon/"

async def get_pokemon(client, url):
    resp = await client.get(url)
    pokemon = resp.json()

    return pokemon['name']

async def poke_multi_async():

    async with httpx.AsyncClient() as client:
        tasks = []
        for number in range(1, 151):
            tasks.append(asyncio.ensure_future(get_pokemon(client,
                         f"{base_url}{number}")))

        original_pokemon = await asyncio.gather(*tasks)
        for pokemon in original_pokemon:
            print(pokemon)

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
results.append(time_func(poke_multi_async, True))

print('\n'.join(results))
