import os
from pathlib import Path

import discord
from discord import app_commands

BASE_DIR = Path(__file__).parent
HALL_IMAGE = BASE_DIR / "hall_da_fama.png"
WELCOME_IMAGE = BASE_DIR / "boas_vindas.png"

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
    try:
        synced = await tree.sync()
        print(f"Bot conectado como {client.user}. {len(synced)} comandos sincronizados.")
    except Exception as error:
        print(f"Erro ao sincronizar comandos: {error}")


@tree.command(name="friendly", description="Anuncia um amistoso preparatório")
async def friendly(interaction: discord.Interaction):
    message = (
        "⚽ **FRIENDLY +7**\n\n"
        "@everyone\n\n"
        "Atenção, jogadores!\n\n"
        "Aqui é o Carlo Ancelotti. Precisamos de comprometimento, união e vontade de vencer.\n\n"
        "Quero todos preparados para mais um desafio. Representem essa seleção com orgulho "
        "e mostrem dentro de campo do que somos capazes!\n\n"
        "VAMOS JOGAR, BRASIL! 🇧🇷🏆\n\n"
        "— Carlo Ancelotti"
    )
    await interaction.response.send_message(
        message,
        allowed_mentions=discord.AllowedMentions(everyone=True)
    )


@tree.command(name="hall_da_fama", description="Apresenta as lendas do Brasil")
async def hall_da_fama(interaction: discord.Interaction):
    embed = discord.Embed(
        title="👑 HALL DA FAMA — BRASIL 🇧🇷",
        description=(
            "# Kaikeoovincius 👑\n"
            "2 bolas de ouro\n"
            "Brasileiro mais Reconhecido Do game e da PSl\n"
            "1 título de SFL\n\n"
            "# Firipe ⚽\n"
            "Jogador Mais experiente BR em atividade campeão PFL ( liga comp) "
            "O mais Reconhecido BR Também e da PSL\n\n"
            "# Carlos Miguel 🗼👑\n"
            "Melhor manager BR que já existiu quase conquistando a copa América "
            "na época de ouro do puresoccer Caindo nas Semifinais\n\n"
            "# Wal 🌿⚽\n"
            "Um dos Melhores Skillers E uns Dos BR mais dribladores com uma história gigante aqui\n\n"
            "# Hydra ☠️👑\n"
            "Melhor CB Br que já teve tanto na PSL e BR tendo sido muitas vezes capitão "
            "da CBF (antiga) e liderando muitas vezes o time em momentos de Pressão\n\n"
            "# Kaka ⚽🌿\n"
            "Um Dos melhores e mais técnicos BR que já existiram com vários MOTM na PFF "
            "com Época de ouro e Diversos reconhecimentos pela habilidade no jogo e história\n\n"
            "# Snoopy🎯\n"
            "O melhores Centro Avante que o Brasil já teve em seus momentos que precisávamos "
            "e em copa América em momentos de Pressão e angústia ele tinha o chute como principal"
        ),
        color=discord.Color.gold()
    )

    if HALL_IMAGE.is_file():
        image = discord.File(HALL_IMAGE, filename="hall_da_fama.png")
        embed.set_image(url="attachment://hall_da_fama.png")
        await interaction.response.send_message(embed=embed, file=image)
    else:
        await interaction.response.send_message(embed=embed)


@tree.command(name="conquistas", description="Mostra as conquistas da Seleção")
async def conquistas(interaction: discord.Interaction):
    message = (
        "🏆 **CONQUISTA — COPA AMÉRICA 2025** 🇧🇷\n\n"
        "🥉 **SEMIFINALISTA — SÉRIE R**\n\n"
        "O Brasil chegou até as semifinais da Copa América 2025, encerrando sua trajetória "
        "entre as melhores seleções da competição.\n\n"
        "🇧🇷⚽ Uma campanha que merece reconhecimento!"
    )
    await interaction.response.send_message(message)


@tree.command(name="bem_vindo", description="Publica o comunicado oficial de boas-vindas")
async def bem_vindo(interaction: discord.Interaction):
    message = (
        "🇧🇷 **CONFEDERAÇÃO BRASILEIRA DE FUTEBOL**\n"
        "⚽ **COMUNICADO OFICIAL — SEJAM BEM-VINDOS!**\n\n"
        "A Seleção Brasileira dá as boas-vindas a todos os novos integrantes que passam "
        "a fazer parte da nossa comunidade!\n\n"
        "Estamos construindo um grupo que representa as cores do Brasil, com jogadores "
        "dispostos a competir, evoluir e escrever uma história dentro do futebol.\n\n"
        "Mais do que jogadores, buscamos companheiros que entendam a importância da união, "
        "do respeito, da disciplina e do comprometimento com a equipe.\n\n"
        "Cada integrante tem um papel importante. Queremos que todos tenham espaço para "
        "mostrar seu futebol, desenvolver suas habilidades e contribuir para o crescimento "
        "da seleção.\n\n"
        "Que essa nova etapa seja marcada por grandes amistosos, competições, vitórias e "
        "momentos que ficarão na memória de todos!\n\n"
        "💚 Honrem a camisa. Respeitem o escudo. Representem o Brasil! 💛\n\n"
        "🤝 Sejam todos muito bem-vindos!\n\n"
        "— Comissão Técnica\n"
        "🇧🇷 Carlo Ancelotti"
    )

    if WELCOME_IMAGE.is_file():
        image = discord.File(WELCOME_IMAGE, filename="boas_vindas.png")
        await interaction.response.send_message(content=message, file=image)
    else:
        await interaction.response.send_message(message)


if __name__ == "__main__":
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        raise RuntimeError(
            "Defina a variável de ambiente DISCORD_TOKEN com o token do seu bot."
        )
    client.run(token)
