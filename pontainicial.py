"""
I/O -> TROCA DE INFORMACOES ENTRE SISTEMAS, trocas assincronas

#Tipos de I/O:
I/O -> busca em banco de dados
I/O -> Chamada a API externa

I/O -> Geralmente eh a troca de um sistema com seu terceiro

executar
chamar uma api() I/O -> Bloqueante
chamar outra api() I/O -> Bloqueante(Parar para continuar processando)

executar
chamar uma api() chamar um banco() I/O -> Nao Bloqueante(Troca de informacoes sem bloquear nenhuma chamada)

#Assincrono
Cria um Event Loop, com Ready Queue(fila de processos) e Timers Queue(fila esperando a resposta)

#Await mais usado em chamada de banco de dados

"""

#Exemplos

import asyncio

# coroutine
async def say_hello(name):
    print(f"{name} is starting...")
    await asyncio.sleep(2) # Simulando IO
    print(f"{name} says hello!")

# coroutine
async def main():
    await say_hello("Rodando sozinho zum") #Sincrono
    await asyncio.gather( #Junta para ser assincrono
        say_hello("Diogo"),
        say_hello("Mariana"),
        say_hello("Adriana"),
        say_hello("Jose")
    )

asyncio.run(main())