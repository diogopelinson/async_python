import asyncio
import httpx #Lib para fazer requicoes assincronas\
import json

async def fetch_get(client:any, pokemon_name: str):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = await client.get(url)
    data = response.json()
    name = data["name"]
    height = data["height"]
    weight = data["weight"]
    moves = data["moves"][1]["move"]
    print(f"name: {name} | height: {height} | weight: {weight} | moves: {moves}")



async def main():
    try:
        async with httpx.AsyncClient() as client:
            await asyncio.gather(
                fetch_get(client, "mew")
            )
    except json.JSONDecodeError:
        print("Pokemon nao encontrado")




asyncio.run(main())