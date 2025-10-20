import asyncio
import httpx #Lib para fazer requicoes assincronas\
import json

async def fetch_get(client: any, pokemon_name:str):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = await client.get(url) # fazendo I/O, sempre que for esperar a resposta de um I/O colocar await
    data = response.json()
    name = data["name"]
    hability = data["moves"][0]["move"]
    print(f"name: {name} | Move: {hability}")

async def main():
    try:
        async with httpx.AsyncClient() as client: #Pegando um cliente assincrono, na documentacao
            await asyncio.gather(
                fetch_get(client, "mewtwo"),
                fetch_get(client, "greninja"),
                fetch_get(client, "xerneas")
            )
            print("Tarefas finalizadas")
    except json.JSONDecodeError:
        print("Pokemon nao encontrado")



asyncio.run(main())