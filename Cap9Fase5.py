import random
import time
from collections import deque


def gerarOrdensDeCarga(maxMercadorias):
    numMercadorias = random.randint(1, maxMercadorias)
    ordens = [f"Mercadoria{i + 1}" for i in range(numMercadorias)]
    return ordens


def calcularTempoCarregamento(rm):
    lastTwoDigits = int(rm[-2:])
    x = (lastTwoDigits % 3) + 1
    return x


def main():
    horaChegadaVan = 20
    horaInicioCarga = 20
    minInicioCarga = 10
    maxMercadorias = 15

    rmAluno = input("Digite o RM do aluno (no formato RMXXXXX): ")[2:]

    ordensDeCarga = deque(gerarOrdensDeCarga(maxMercadorias))
    filaEspera = deque()

    numMercadoriasGeradas = len(ordensDeCarga)

    print(f"Horário de chegada da van: {horaChegadaVan}:00")
    print(f"RM escolhido: RM{rmAluno}")
    print(f"Número de mercadorias geradas aleatoriamente: {numMercadoriasGeradas}")

    tempoTotal = 0
    numMercadoriasCarregadas = 0

    while ordensDeCarga or filaEspera:
        # Adiciona itens da ordem de carga à fila de espera se houver menos de 3 mercadorias na fila de espera
        while ordensDeCarga and len(filaEspera) < 3:
            if len(ordensDeCarga) >= 3:
                for _ in range(3):
                    mercadoria = ordensDeCarga.popleft()
                    filaEspera.append(mercadoria)
                    print(f"'{mercadoria}' foi para a fila de espera.")
            else:
                filaEspera.extend(ordensDeCarga)
                ordensDeCarga.clear()

        # Início da carga às 20:10
        if tempoTotal == 0 and horaChegadaVan == horaInicioCarga:
            tempoTotal = minInicioCarga  # A carga inicia 10 minutos após a chegada da van às 20:00

        # Calcula o tempo de carregamento com base no RM do aluno
        tempoCarga = calcularTempoCarregamento(rmAluno)

        # Realiza a carga
        if filaEspera:
            mercadoria = filaEspera.popleft()
            numMercadoriasNaOrdem = len(ordensDeCarga) + len(filaEspera) + 1
            print(
                f"\nIniciando carga da '{mercadoria}' (Ordem de Carga com {numMercadoriasNaOrdem} mercadorias) às {horaInicioCarga}:{tempoTotal:02}")
            print(f"Tempo de carregamento: {tempoCarga} minutos")
            tempoTotal += tempoCarga
            numMercadoriasCarregadas += 1
            print(f"Tempo total de carregamento acumulado: {tempoTotal} minutos")
            print(f"Número de mercadorias na fila de espera: {len(filaEspera)}")

        # A cada 2 minutos, o primeiro item da fila de ordem de cargas vai para a fila de espera
        if tempoTotal % 2 == 0 and ordensDeCarga:
            mercadoria = ordensDeCarga.popleft()
            filaEspera.append(mercadoria)
            print(f"'{mercadoria}' foi para a fila de espera.")

        # Verifica se a carga está completa
        if not ordensDeCarga and not filaEspera:
            print("\nCarga completa!")
            print(f"Número total de mercadorias carregadas: {numMercadoriasCarregadas}")


if __name__ == "__main__":
    main()

