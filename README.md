# PasarRato v5.0 ⚔️

![Version](https://img.shields.io/badge/Version-5.0-blue)
![Python](https://img.shields.io/badge/Python-3.11_Strict-yellow)
![Status](https://img.shields.io/badge/Status-Refactoring_Pending-orange)

**Spanish README:** Please refer to the [README_es.md](./README_es.md) file in this repository.

Console game developed in Python with a focus on turn-based combat mechanics and stat scaling. Designed with a modular architecture, the project explores Technical Game Design mechanics (class balance, difficulty scaling, and risk/reward economy) on a solid Software Engineering foundation.

> ⚠️ **PROJECT STATUS AND TECHNICAL DEBT (Pygame Refactoring)**
> Currently, the game **is not executable on the most recent versions of Python**. The audio and event engine based on `pygame.mixer` requires a technical refactoring to meet the initialization standards of modern library versions. 
> *Temporary solution:* The project must be run **strictly on Python 3.11** using an isolated virtual environment until the compatibility patch is released.

---

## 🚀 What's New in Version 5.0: i18n Architecture
The main update of this version is the implementation of a **dynamic internationalization (i18n) system**. Through the `translation.py` script, the game now supports the dynamic injection of texts to alternate between **Spanish and English** in real time, without mutating the core logic of the *game loop* or affecting the rendering of the interface.

---

## 🎲 Core Loop and Mechanics (Game Design)

The game design is centered around an automated combat *Core Loop* with tactical player interventions at key moments.

*   **Main Loop:**
    1.  Zone Scaling: The player traverses 3 distinct zones (Lonely Plains, Cursed Forest, Abandoned Castle) divided into 5 rounds of regular combat, where enemy HP and damage scale progressively.
    2.  Boss Fight (Round 6): A final combat that introduces the "Shield" mechanic and where the Power Spikes (Special Abilities) of each class are activated.
    3.  Economy and Progression: At the end of each round, the player obtains coins based on their performance (remaining HP). These resources feed a risk/reward system in the shop such as purchasing fixed stats or the option to use an RNG system to obtain huge improvements (massive Buffs) or suffer penalties (Debuffs).
*   **Class Balance (Strategic Asymmetry):**
    *   🥊 **Brawler:** Balanced attributes (HP: 2500, Damage: ~600). *Ability:* Generates extra gold if they survive with more than 1000 HP.
    *   🥷 **Assassin:** Glass cannon (HP: 1500, Damage: ~750). *Ability (Lethal Attack):* Triples their damage on the second turn against the boss.
    *   🛡️ **Tank:** Mitigation wall (HP: 4500, Damage: ~300). *Ability (Duo Strike):* Temporarily summons another class for a combined attack on turn 4 of the boss.
    *   🏹 **Marksman:** Sustained damage (HP: 2000, Damage: ~400 x shot). *Ability (Tic Tac):* Attacks 4 consecutive times on the fourth turn of the boss.

---

## 🏗️ Modular Architecture (SWE)

The source code is structured in a modular way to separate concerns (SoC), facilitating maintenance and future expansions:
*   `pasarrato.py`: Main game loop, state machine, and round transition manager.
*   `text.py`: Deep combat logic, damage calculations, RNG events, class abilities, and map rendering (ASCII Art).
*   `funciones.py`: Manual implementation of data structures (`Stack`, `Queue`) and cross-platform I/O clearing utilities.
*   `money.py` and `valores.py`: Global state controllers and injection of the shop's transactional logic.
*   `music.py`: Wrapper of `pygame.mixer` for audio thread management (Soundtrack, SFX, and character voices).
*   `menu_interactive.py`: Reactive UI rendering using the `keyboard` library for fluid console control.

---

## ⚙️ Requirements and Installation

Due to the aforementioned technical debt, it is highly recommended to use a virtual environment (venv).

**Dependencies:**
*   Python 3.11 (Strict)
*   keyboard 0.13.5
*   pygame 2.5.2

**Installation Steps:**
1. Clone the repository.
   ```bash
   git clone https://github.com/AimLion/PasarRato.git
   ```
2. Create a virtual environment (Requires Python 3.11).
   ```powershell
   python -m venv pasarrato
   ```
3. Activate the environment and install the exact dependencies.
   ```powershell
   .\pasarrato\Scripts\activate
   
   pip install -r requirements.txt
   ```
4. Execute the main loop.
   ```powershell
   python pasarrato.py
   ```

---

## 🎵 Credits and Attribution (Fair Use)

The sonic identity of this project uses *assets* for strictly educational and non-commercial purposes, under the principle of *Fair Use*. The intellectual property rights of all sounds and musical themes included in this project belong to their author/company:
*   **Toby Fox** (Effects and themes from *Undertale*).
*   **Phoenix Network** (Menu music from *Galaxy Life*).
*   **Riot Games** (Voices and effects from *League of Legends*).

*If you are the owner of these rights and wish for the sounds to be removed from this project, please contact me at maximus.jasso@gmail.com and I will proceed to remove them.*

Last modification: September - 2026