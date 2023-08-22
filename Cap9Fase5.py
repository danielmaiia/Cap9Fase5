import random
import time


def carregar_mercadorias():
    return random.randint(1, 15)


def main():
    rm_ultimo_digito = 11  # Últimos dois dígitos do RM 96111
    X = (rm_ultimo_digito % 100) % 3 + 1  # Tempo de carregamento das mercadorias

    fila_de_carga = []
    tempo = 0
    iterações = 0
    while True:
        if iterações % 10 == 0:  # A cada 10 iterações, avança 1 minuto no relógio
            tempo += 1

        # Adiciona mercadorias à fila de carga a cada 2 minutos
        if tempo % 2 == 0:
            num_mercadorias = carregar_mercadorias()  # Gera o número de mercadorias a serem adicionadas
            fila_de_carga.extend([X] * num_mercadorias)  # Adiciona as mercadorias à fila

        # Carrega as mercadorias na van
        if fila_de_carga:
            while len(fila_de_carga) >= 3:
                carregadas = fila_de_carga[:3]  # Pega as próximas 3 mercadorias da fila
                fila_de_carga = fila_de_carga[3:]  # Remove as mercadorias carregadas da fila
                tempo_de_carga = max(carregadas) * X  # Calcula o tempo de carga com base na mercadoria mais demorada
                tempo += tempo_de_carga

                print(f"{tempo // 60:02d}:{tempo % 60:02d} - Carregadas {len(carregadas)} mercadorias.")

        # Verifica se não há mais mercadorias na fila
        if not fila_de_carga:
            break

        iterações += 1
        time.sleep(1)  # Aguarda 1 segundo para simular o avanço de 1 minuto


if __name__ == "__main__":
    main()

