def compara(a, b):
    if a["razaoPontoTempo"] == b["razaoPontoTempo"]:
        return 0
    elif a["razaoPontoTempo"] > b["razaoPontoTempo"]:
        return -1
    else:
        return 1

def main():
    instancia = 0
    while True:
        qtsAtracoes, limiteTempo = map(int, input().split())

        if qtsAtracoes == 0:
            break

        brinquedos = []

        for _ in range(qtsAtracoes):
            tempo, qtsPontos = map(int, input().split())
            razaoPontoTempo = qtsPontos / tempo
            brinquedos.append({"tempo": tempo, "qtsPontos": qtsPontos, "razaoPontoTempo": razaoPontoTempo})

        brinquedos.sort(key=lambda x: x["razaoPontoTempo"], reverse=True)

        i = 0
        pontoTotal = tempoTotal = 0

        while i < qtsAtracoes:
            aux = tempoTotal + brinquedos[i]["tempo"]

            if aux <= limiteTempo:
                pontoTotal += brinquedos[i]["qtsPontos"]
                tempoTotal = aux
            else:
                i += 1

        instancia += 1
        print(f"Instancia {instancia}")
        print(pontoTotal)
        print()

if __name__ == "__main__":
    main()
