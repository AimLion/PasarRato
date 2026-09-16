idioma_actual = "Español"

def Translate():
    global idioma_actual
    idioma_actual = {"Español": "English", "English": "Español"}[idioma_actual]
    print(f"\nIdioma cambiado a: {idioma_actual}")

def TxtPrint(Id_txt, **kwargs ):
    texto_base = TRADUCCIONES.get(idioma_actual, {}).get(Id_txt, Id_txt)
    return texto_base.format(**kwargs)
# TODO Categorizar los textos con {} para secciones de menu, combate, personajes, etc.
# y poder traducirlos de manera más eficiente. Buscar forma de darle color ANSI a la terminal
TRADUCCIONES = {
    "Español": {
        "main_menu" : (
            "Bienvenido al Sistema de Combate Automatizado\n"
            "#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#\n\n"

            "Menu de opciones\n"
            "1) Iniciar Partida\n"
            "2) Comprar Mejoras ( ${cantm} monedas )\n"
            "3) Cambiar de personaje ({personaje})\n"
            "4) Cambiar al idioma Ingles\n"
            "5) Salir"
        ),
        "select_menu" : "\nSeleccione una opción del menú: ",
        "invalid_option" : "\nOpción inválida. Intente de nuevo.",
        "logout" : "Vuelva Pronto!!!",
        "loading_characters" : "\nCargando personajes . . .",
        "loading_combat" : "Cargando combate . . .",
        "validation_upgrade" : "\nYa tienes una mejora!",
        "check_combat" : "\n¿Listo para el combate? (S/N) → ",
        "ready_combat" : "\nInicia Combate!! Ronda {Round}",
        "values_character" : "\nTu vida: {vidaPJ}  Su vida: {vidaE}",
        "check_shield" : "¿Quieres usar el escudo en este ataque?: (s/n)\n",
        "blocked_damage" : "Has bloqueado {ataqueE} de daño!",
        "health_boss" : "\n¡¡El enemigo a regenerado 1500 de vida!!",
        "health_option" : "\n¿Quieres curarte? (S/N) → ",
        "life_restored" : "\n¡¡Haz recuperado {curacion} de vida!!",
        "surrender_option" : "\n¿Quieres retirarte (S/N) → ",
        "penalty_gameover" : "\nPenalización de Gameover - Monedas / 2\nMonedas: {monedas}",
        "win_boss" : "Lograste derrotar al jefe!! ( + $150 monedas )",
        "jefe_txt0" : "\nAlgo pasa . . .",
        "jefe_txt1" : "Este nivel no debería existir . . .",
        "jefe_txt2" : "\n-Sientes corrientes de viento rodeandote- . . .",
        "jefe_txt3" : "\nLos enemigos no están . . .",
        "jefe_txt4" : "A donde se han ido? . . .",
        "jefe_txt5" : "\n-Una voz se escucha al fondo- . . .",
        "jefe_txt6" : "\nTodos se han reunido contra ti . . .",
        "jefe_txt7" : "Esta es la batalla final . . .",
        "victory_message" : "\nGran combate!! Has sobrevivido {z} turnos con {vidaPJ} de vida",
        "draw_message" : "\nA sido un gran combate, se declara un empate.",
        "defeat_message" : "\nBuen intento, ha sobrevivido el enemigo con {vidaE} de vida",
        "round_zone_message" : "\nLlegaste hasta el round {Round} En la zona {zona}",
        "player_dmg_message" : "\nCantidad de daño infligido: {registroPJ} Total → {totalPJ}",
        "enemy_dmg_message" : "Cantidad de daño del enemigo: {registroE} Total → {totalE}",
        "player_avg_dmg_message" : "\nTu daño promedio: {ApromPJ}",
        "enemy_avg_dmg_message" : "Daño promedio del enemigo: {ApromE}",
        "attacked_enemy_message" : "El enemigo te a bajado {ataqueE} de vida",
        "oneshot_message" : "\nHAS ONESHOTEADO AL ENEMIGO!! +$100",
        "map_levels" : "\nMapa de niveles",
        "zone1_name" : "Las Llanuras Solitarias",
        "zone2_name" : "El Bosque Maldito",
        "zone3_name" : "El Castillo Abandonado",
        "actual_zone" : "\nEstás en {nombre}!!",
        "attacked_message" : "Has infligido {ataquePJ} de daño al enemigo",
        "attacked_shooter_message" : "Le has bajado {ataquePJ} y {ataquePJ2} de vida al enemigo",
        "attacked_tank_message" : "Tu y el {duopj} le han bajado {ataquePJ} de vida al enemigo!!",
        "special_abiliti_fighter" : "Has ganado +${comision} por \"Mi comisión!\"",
        "special_abiliti_assassin" : "\"Ataque Letal\" del {personaje}!!",
        "special_abiliti_tank" : "\"Golpe Duo\" del {personaje}!!\n",
        "special_abiliti_shooter" : "\"Tic . . .Tac . . .\" del {personaje}!!",
        "first_atk_shooter" : "\nPrimer Disparo de {ataquePJ} !",
        "Second_atk_shooter" : "Segundo Disparo de {numAtaque} !!",
        "Third_atk_shooter" : "Tercer Disparo de {numAtaque} !!!",
        "fourth_atk_shooter" : "Cuarto Disparo de {numAtaque} !!!",
        "menu_upgrade" : (
            "Menu de Mejoras\n"
            "#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#\n\n"

            "Monedas: ${money}\n\n"
            "Opciones:\n"
            "1) Aumentar Ataque +150 - Precio $250\n"
            "2) Aumentar Vida +250 - Precio $150\n"
            "3) Bloquear un Ataque del Jefe - Precio $500\n"
            "4) Probar la Catafixia\n"
            "5) Regresar al Menu Principal"
        ),
        "return_menu" : "\nRegresando al menu . . .",
        "upgrade1_success" : "\nMejora de Ataque +150 adquirida!!",
        "upgrade2_success" : "\nMejora de Vida +250 adquirida!!",
        "upgrade3_success" : "\nHas adquirido un escudo consumible por 1 ataque del jefe!!",
        "loading_catafixia" : "\nCargando Catafixia . . .",
        "round_money" : "\nHas obtenido ${RoundMoney} monedas!",
        "succesful_purchase" : "\nLa compra fue exitosa!!",
        "unsuccesful_purchase" : "\nNo tienes suficientes monedas para esta compra.",
        "welcome_catafixia" : "Bienvenido a la Catafixia!",
        "activate_catafixia" : "\nPulsa la tecla espacio para sacar tu ficha",
        "selected_box" : "\nTomaste la ficha número: {caja}",
        "show_box" : "\n¿Qué has ganado? . . .",
        "buff_message" : "\nHas ganado {caja}",
        "nerf_message" : "\nLastima, {caja}",
        "boxBuff_1" : "Una espada de fuego!! (+500 ataque)",
        "boxBuff_2" : "Una poción bonificadora (+500 hp)",
        "boxBuff_3" : "Un escudo",
        "show_other_boxes" : "\n¿Que había en las demás cajas?\n",
        "content_boxes" : "En la caja {caja} había: {contenido}",
        "menu_characters" : (
            "Menu de Selección de personaje\n"
            "#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#\n"

            "Escoje tu personaje"
        ),
        "coins_available" : "\nMonedas disponibles: ${money}",
        "instructions_menu" : "\n-) Pulsa enter para elegir/comprar\n-) Pulsa tab para regresar al menú",
        "loading_character" : "Cargando personaje . . .",
        "character_info" : (
            "Personaje - El {namePj}"
            "\nInformación General:\n {descrip}"

            "\n\nOpciones:\n"
            "1) Seleccionar\n"
            "2) Regresar\n"
            "\nSelecciona: "
        ),
        "character_selected" : "\nElegiste al {namePj}",
        "description_fighter" : (
            "\n- Este peleador a estado en infinidad de combates, la experiencia que a obtenido más la fuerza lo vuelven el peleador más potente de toda la arena.\n"
            "\nDatos de Batalla:\n - Vida Maxima: 2500\n - Daño Promedio: 600 (+- 100)\n - Habilidad Especial: \"Mi comisión!\"\n   Si al final de cada ronda queda con más de 1000 de vida, obtendrá +$50 de monedas y 150 si vence al jefe con la misma condición."),
        "description_assassin" : (
            "\n- Este feroz asesino es sigiloso cual noche y puede eliminar a sus enemigos sin que lleguen a sentir su presencia. Un golpe certero y no se levantarán tus contrincantes\n"
            "\nDatos de Batalla:\n - Vida Maxima: 1500\n - Daño Promedio: 750 (+- 100)\n - Habilidad Especial: \"Ataque Letal\"\n   Después de 2 turnos contra el jefe, se esconde para lanzar un ataque con el daño triplicado."
        ),
        "description_tank" : (
            "\n- Este robusto tanque es como ningún otro. Si bien no puede aplicar mucho daño, lo fuerte en él es su aguante y espiritu por luchar. Llévalo a la arena y solo te harán cosquillas tus enemigos\n"
            "\nDatos de Batalla:\n - Vida Maxima: 4500\n - Daño Promedio: 300 (+- 100)\n - Habilidad Especial: \"Golpe Duo\"\n   Después de 4 turnos contra el jefe, llama a un compañero al azar para atacar juntos."
        ),
        "description_shooter" : (
            "\n- Sin duda alguna, no hay nadie como este tirador. Sea en lluvia o tormenta, nunca dejaría ir a sus enemigos con vida. Puedes llevarlo a la arena y cada tiro será una victoria a la lista.\n"
            "\nDatos de Batalla:\n - Vida Maxima: 2000\n - Daño Promedio: 400 (+- 100) x Disparo\n - Habilidad Especial: \"Tic tac\"\n   Ataca dos veces por turno, y en el turno 4 contra el jefe, ataca cuatro veces seguidas."
        )
    },
    "English": {
        "main_menu": (
            "Welcome to the Automated Combat System\n"
            "#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#\n\n"

            "Options Menu\n"
            "1) Start Game\n"
            "2) Buy Upgrades ( ${cantm} coins )\n"
            "3) Change character ({personaje})\n"
            "4) Change to Spanish language\n"
            "5) Exit"
        ),
        "select_menu": "\nSelect a menu option: ",
        "invalid_option": "\nInvalid option. Try again.",
        "logout": "Come back soon!!!",
        "loading_characters": "\nLoading characters . . .",
        "loading_combat": "Loading combat . . .",
        "validation_upgrade": "\nYou already have an upgrade!",
        "check_combat": "\nReady for combat? (Y/N) → ",
        "ready_combat": "\nCombat Starts!! Round {Round}",
        "values_character": "\nYour health: {vidaPJ}  Enemy health: {vidaE}",
        "check_shield": "Do you want to use the shield for this attack? (y/n)\n",
        "blocked_damage": "You have blocked {ataqueE} damage!",
        "health_boss": "\nThe enemy has regenerated 1500 health!!",
        "health_option": "\nDo you want to heal? (Y/N) → ",
        "life_restored": "\nYou have recovered {curacion} health!!",
        "surrender_option": "\nDo you want to retreat? (Y/N) → ",
        "penalty_gameover": "\nGame Over Penalty - Coins / 2\nCoins: {monedas}",
        "win_boss": "You managed to defeat the boss!! ( + $150 coins )",
        "jefe_txt0": "\nSomething is happening . . .",
        "jefe_txt1": "This level shouldn't exist . . .",
        "jefe_txt2": "\n-You feel wind currents surrounding you- . . .",
        "jefe_txt3": "\nThe enemies are gone . . .",
        "jefe_txt4": "Where have they gone? . . .",
        "jefe_txt5": "\n-A voice is heard in the background- . . .",
        "jefe_txt6": "\nEveryone has gathered against you . . .",
        "jefe_txt7": "This is the final battle . . .",
        "victory_message": "\nGreat combat!! You survived {z} turns with {vidaPJ} health",
        "draw_message": "\nIt has been a great combat, a draw is declared.",
        "defeat_message": "\nGood try, the enemy survived with {vidaE} health",
        "round_zone_message": "\nYou made it to round {Round} in zone {zona}",
        "player_dmg_message": "\nAmount of damage dealt: {registroPJ} Total → {totalPJ}",
        "enemy_dmg_message": "Amount of enemy damage: {registroE} Total → {totalE}",
        "player_avg_dmg_message": "\nYour average damage: {ApromPJ}",
        "enemy_avg_dmg_message": "Enemy's average damage: {ApromE}",
        "attacked_enemy_message": "The enemy has taken {ataqueE} of your health",
        "oneshot_message": "\nYOU ONE-SHOTTED THE ENEMY!! +$100",
        "map_levels": "\nLevel Map",
        "zone1_name": "The Lonely Plains",
        "zone2_name": "The Cursed Forest",
        "zone3_name": "The Abandoned Castle",
        "actual_zone": "\nYou are in {nombre}!!",
        "attacked_message": "You dealt {ataquePJ} damage to the enemy",
        "attacked_shooter_message": "You took {ataquePJ} and {ataquePJ2} health from the enemy",
        "attacked_tank_message": "You and the {duopj} took {ataquePJ} health from the enemy!!",
        "special_abiliti_fighter": "You gained +${comision} for \"My commission!\"",
        "special_abiliti_assassin": "\"Lethal Attack\" from {personaje}!!",
        "special_abiliti_tank": "\"Duo Strike\" from {personaje}!!\n",
        "special_abiliti_shooter": "\"Tick . . . Tock . . .\" from {personaje}!!",
        "first_atk_shooter": "\nFirst Shot of {ataquePJ} !",
        "Second_atk_shooter": "Second Shot of {numAtaque} !!",
        "Third_atk_shooter": "Third Shot of {numAtaque} !!!",
        "fourth_atk_shooter": "Fourth Shot of {numAtaque} !!!",
        "menu_upgrade": (
            "Upgrades Menu\n"
            "#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#\n\n"

            "Coins: ${money}\n\n"
            "Options:\n"
            "1) Increase Attack +150 - Price $250\n"
            "2) Increase Health +250 - Price $150\n"
            "3) Block one Boss Attack - Price $500\n"
            "4) Try the Catafixia\n"
            "5) Return to Main Menu"
        ),
        "return_menu": "\nReturning to menu . . .",
        "upgrade1_success": "\nAttack Upgrade +150 acquired!!",
        "upgrade2_success": "\nHealth Upgrade +250 acquired!!",
        "upgrade3_success": "\nYou have acquired a consumable shield for 1 boss attack!!",
        "loading_catafixia": "\nLoading Catafixia . . .",
        "round_money": "\nYou have obtained ${RoundMoney} coins!",
        "succesful_purchase": "\nThe purchase was successful!!",
        "unsuccesful_purchase": "\nYou do not have enough coins for this purchase.",
        "welcome_catafixia": "Welcome to the Catafixia!",
        "activate_catafixia": "\nPress the spacebar to draw your token",
        "selected_box": "\nYou took token number: {caja}",
        "show_box": "\nWhat have you won? . . .",
        "buff_message": "\nYou have won {caja}",
        "nerf_message": "\nToo bad, {caja}",
        "boxBuff_1": "A fire sword!! (+500 attack)",
        "boxBuff_2": "A bonus potion (+500 hp)",
        "boxBuff_3": "A shield",
        "show_other_boxes": "\nWhat was in the other boxes?\n",
        "content_boxes": "In box {caja} there was: {contenido}",
        "menu_characters": (
            "Characters Selection Menu\n"
            "#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#\n"

            "Choose your Characters"
        ),
        "coins_available": "\nAvailable coins: ${money}",
        "instructions_menu": "\n-) Press enter to choose/buy\n-) Press tab to return to the menu",
        "loading_character": "Loading Characters . . .",
        "character_info": (
            "Character - The {namePj}"
            "\nGeneral Information:\n {descrip}"

            "\n\nOptions:\n"
            "1) Select\n"
            "2) Return\n"
            "\nSelect: "
        ),
        "character_selected": "\nYou chose the {namePj}",
        "description_fighter": (
            "\n- This fighter has been in countless combats, the experience he has gained plus his strength make him the most powerful fighter in the entire arena.\n"
            "\nCombat Data:\n - Max Health: 2500\n - Average Damage: 600 (+- 100)\n - Special Ability: \"My commission!\"\n   If at the end of each round he has more than 1000 health, he will get +$50 coins, and 150 if he beats the boss under the same condition."
        ),
        "description_assassin": (
            "\n- This fierce assassin is stealthy like the night and can eliminate his enemies without them ever feeling his presence. A precise strike and your opponents won't get up.\n"
            "\nCombat Data:\n - Max Health: 1500\n - Average Damage: 750 (+- 100)\n - Special Ability: \"Lethal Attack\"\n   After 2 turns against the boss, he hides to launch an attack with tripled damage."
        ),
        "description_tank": (
            "\n- This sturdy tank is like no other. While he can't deal much damage, his strength lies in his endurance and fighting spirit. Take him to the arena and your enemies will only tickle you.\n"
            "\nCombat Data:\n - Max Health: 4500\n - Average Damage: 300 (+- 100)\n - Special Ability: \"Duo Strike\"\n   After 4 turns against the boss, he calls a random companion to attack together."
        ),
        "description_shooter": (
            "\n- Without a doubt, there is no one like this shooter. Be it in rain or storm, he would never let his enemies leave alive. You can take him to the arena and every shot will be a victory added to the list.\n"
            "\nCombat Data:\n - Max Health: 2000\n - Average Damage: 400 (+- 100) x Shot\n - Special Ability: \"Tick tock\"\n   Attacks twice per turn, and on turn 4 against the boss, attacks four times in a row."
        )
    }
}
