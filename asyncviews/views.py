from django.http import HttpResponse
import asyncio
import httpx


async def http_call_async():
    for num in range(0, 6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get('https://httpbin.org')
        print(r)


async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse("Função assíncrona criada com sucesso!!!")
