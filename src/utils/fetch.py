import asyncio

# Fetches a single url
async def fetch(session, url: str):
    async with session.get(url) as response:
        if response.status != 200:
            # response.raise_for_status()
            print( Exception(f"Error fetching {url}: status {response.status}"))

        print (f"Success fetching {url}")
        return await response.json()

async def fetch_all(session, urls):
    tasks = []
    for url in urls:
        task = await asyncio.create_task(fetch(session, url))
        tasks.append(task)
    results = await asyncio.gather(*tasks, return_exceptions=False)
    return results