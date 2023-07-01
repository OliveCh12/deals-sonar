import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        data = await response.json()
        return data

async def fetch_all_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.ensure_future(fetch_url(session, url))
            tasks.append(task)
        
        results = await asyncio.gather(*tasks)
        return results

# Liste des URL à récupérer
urls = [
    "https://api.example.com/data1",
    "https://api.example.com/data2",
    "https://api.example.com/data3"
]

loop = asyncio.get_event_loop()
results = loop.run_until_complete(fetch_all_urls(urls))

# Traiter les résultats
for result in results:
    # Faire quelque chose avec les données récupérées
    print(result)
