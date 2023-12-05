def input_dados():
    try:
        idade = int(input("Qual sua idade? (Caso queira encerrar, digite -1): "))
        if idade == -1:
            return None

        sexo = input("Qual seu sexo? M-Masculino, F-Feminino: ").upper()
        rede_social = input("Qual sua rede social preferida? (Facebook/Instagram/Twitter): ").lower()

        return idade, sexo, rede_social

    except ValueError:
        print("Por favor, digite uma idade válida.")
    


def main():
    total_respondentes = 0
    pref_facebook = 0
    pref_instagram = 0
    pref_twitter = 0
    idades_facebook = []
    idades_twitter = []
    idades_instagram = []
    idades_masculino_facebook = 0
    idades_masculino_twitter = 0
    idades_masculino_instagram = 0
    idades_feminino_facebook = 0
    idades_feminino_twitter = 0
    idades_feminino_instagram = 0

    while True:
        dados = input_dados()
        if dados is None:
            break

        idade, sexo, rede_social = dados

        total_respondentes += 1

        if rede_social == 'facebook':
            pref_facebook += 1
            idades_facebook.append(idade)
            if sexo == 'M':
                idades_masculino_facebook += 1
            elif sexo == 'F':
                idades_feminino_facebook += 1

        elif rede_social == 'instagram':
            pref_instagram += 1
            idades_instagram.append(idade)
            if sexo == 'M':
                idades_masculino_instagram += 1
            elif sexo == 'F':
                idades_feminino_instagram += 1

        elif rede_social == 'twitter':
            pref_twitter += 1
            idades_twitter.append(idade)
            if sexo == 'M':
                idades_masculino_twitter += 1
            elif sexo == 'F':
                idades_feminino_twitter += 1

    percent_facebook = (pref_facebook / total_respondentes) * 100
    percent_instagram = (pref_instagram / total_respondentes) * 100
    percent_twitter = (pref_twitter / total_respondentes) * 100

    idade_mais_velho_facebook = max(idades_facebook, default=None)
    idade_mais_velho_instagram = max(idades_instagram, default=None)
    idade_mais_velho_twitter = max(idades_twitter, default=None)

    idade_mais_novo_facebook = min(idades_facebook, default=None)
    idade_mais_novo_instagram = min(idades_instagram, default=None)
    idade_mais_novo_twitter = min(idades_twitter, default=None)

    print("\nResultados:")
    print(f"1. Total de respostas: {total_respondentes}")
    print(f"2. Percentual de que prefere Facebook: {percent_facebook:.2f}%")
    print(f"3. Percentual de que prefere Instagram: {percent_instagram:.2f}%")
    print(f"4. Percentual de que prefere Twitter: {percent_twitter:.2f}%")
    print(f"5. Idade do Mais Velho que Prefere Facebook: {idade_mais_velho_facebook}")
    print(f"6. Idade do Mais Velho que Prefere Twitter: {idade_mais_velho_twitter}")
    print(f"7. Idade do Mais Velho que Prefere Instagram: {idade_mais_velho_instagram}")
    print(f"8. Idade do Mais Novo que Prefere Facebook: {idade_mais_novo_facebook}")
    print(f"9. Idade do Mais Novo que Prefere Twitter: {idade_mais_novo_twitter}")
    print(f"10. Idade do Mais Novo que Prefere Instagram: {idade_mais_novo_instagram}")
    print(f"11. Qntd Homens que Preferem Facebook: {idades_masculino_facebook}")
    print(f"12. Qntd. de Homens que Preferem Twitter: {idades_masculino_twitter}")
    print(f"13. Qntd. de Homens que Preferem Instagram: {idades_masculino_instagram}")
    print(f"14. Qntd. de Mulheres que Preferem Facebook: {idades_feminino_facebook}")
    print(f"15. Qntd. de Mulheres que Preferem Twitter: {idades_feminino_twitter}")
    print(f"16. Qntd. de Mulheres que Preferem Instagram: {idades_feminino_instagram}")


if __name__ == "__main__":
    main()
