def chooseAccessType() -> str:
    accessType = input(
        "\nDigite qualquer coisa para entrar no login do dentista ou tecle [Enter] para entrar no login da recepção: ")

    if len(accessType):
        return "dentist"
    else:
        return "frontDesk"
