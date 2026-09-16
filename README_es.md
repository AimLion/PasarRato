# PasarRato v5.0 ⚔️

![Versión](https://img.shields.io/badge/Versión-5.0-blue)
![Python](https://img.shields.io/badge/Python-3.11_Estricto-yellow)
![Estado](https://img.shields.io/badge/Estado-Refactorización_Pendiente-orange)

Juego de consola desarrollado en Python con un enfoque en mecánicas de combate por turnos y escalado de estadísticas. Diseñado con una arquitectura modular, el proyecto explora mecánicas de Technical Game Design (balance de clases, escalado de dificultad y economía de riesgo/recompensa) sobre una base sólida de Software Engineering.

> ⚠️ **ESTADO DEL PROYECTO Y DEUDA TÉCNICA (Refactorización de Pygame)**
> Actualmente, el juego **no es ejecutable en las versiones más recientes de Python**. El motor de audio y eventos basado en `pygame.mixer` requiere una refactorización técnica para cumplir con los estándares de inicialización de las versiones modernas de la librería. 
> *Solución temporal:* El proyecto debe ejecutarse **estrictamente en Python 3.11** utilizando un entorno virtual aislado hasta que se lance el parche de compatibilidad.

---

## 🚀 Novedades en la Versión 5.0: Arquitectura i18n
La actualización principal de esta versión es la implementación de un **sistema dinámico de internacionalización (i18n)**. Mediante el script `translation.py`, el juego ahora soporta la inyección dinámica de textos para alternar entre **Español e Inglés** en tiempo real, sin mutar la lógica central del *game loop* ni afectar la renderización de la interfaz.

---

## 🎲 Core Loop y Mecánicas (Game Design)

El diseño del juego se centra en un *Core Loop* de combate automatizado con intervenciones tácticas del jugador en momentos clave.

*   **Bucle Principal:**
    1.  Escalado de Zonas: El jugador atraviesa 3 zonas distintas (Llanuras Solitarias, Bosque Maldito, Castillo Abandonado) divididas en 5 rondas de combate regular, donde el HP y daño enemigo escalan progresivamente.
    2.  Boss Fight (Ronda 6): Un combate final que introduce la mecánica de "Escudo" y donde se activan los Power Spikes (Habilidades Especiales) de cada clase.
    3.  Economía y Progresión: Al final de cada ronda, el jugador obtiene monedas basadas en su rendimiento (HP restante). Estos recursos alimentan un sistema de riesgo/recompensa en la tienda como la compra de estadisticas fijas o la opción de usar un sistema RNG para obtener grandes mejoras (Buffs masivos) o sufrir penalizaciones (Debuffs).
*   **Balance de Clases (Asimetría Estratégica):**
    *   🥊 **Peleador:** Atributos balanceados (HP: 2500, Daño: ~600). *Habilidad:* Genera oro extra si sobrevive con más de 1000 HP.
    *   🥷 **Asesino:** Cañón de cristal (HP: 1500, Daño: ~750). *Habilidad (Ataque Letal):* Triplica su daño en el segundo turno contra el jefe.
    *   🛡️ **Tanque:** Muro de mitigación (HP: 4500, Daño: ~300). *Habilidad (Golpe Duo):* Invoca a otra clase temporalmente para un ataque combinado en el turno 4 del jefe.
    *   🏹 **Tirador:** Daño sostenido (HP: 2000, Daño: ~400 x tiro). *Habilidad (Tic Tac):* Ataca 4 veces consecutivas en el cuarto turno del jefe.

---

## 🏗️ Arquitectura Modular (SWE)

El código fuente está estructurado de manera modular para separar responsabilidades (SoC), facilitando el mantenimiento y futuras expansiones:
*   `pasarrato.py`: Bucle principal del juego, máquina de estados y gestor de transiciones de rondas.
*   `text.py`: Lógica profunda del combate, cálculos de daño, eventos RNG, habilidades de clases y renderizado del mapa (ASCII Art).
*   `funciones.py`: Implementación manual de estructuras de datos (`Stack`, `Queue`) y utilidades de limpieza I/O multiplataforma.
*   `money.py` y `valores.py`: Controladores de estado global e inyección de la lógica transaccional de la tienda.
*   `music.py`: Wrapper de pygame.mixer para la gestión de hilos de audio (Banda sonora, SFX, y voces de personajes).
*   `menu_interactive.py`: Renderizado reactivo de la UI usando la librería `keyboard` para un control fluido por consola.

---

## ⚙️ Requisitos e Instalación

Debido a la deuda técnica mencionada, se recomienda encarecidamente utilizar un entorno virtual (venv).

**Dependencias:**
*   Python 3.11 (Estricto)
*   keyboard 0.13.5
*   pygame 2.5.2

**Pasos de Instalación:**
1. Clona el repositorio:
   ```bash
   git clone https://github.com/AimLion/PasarRato.git
   ```
2. Crea un entorno virtual (Requiere Python 3.11):
   ```powershell
   python -m venv pasarrato
   ```
3. Activa el entorno e instala las dependencias exactas:
   ```powershell
   .\pasarrato\Scripts\activate
   
   pip install -r requirements.txt
   ```
4. Ejecuta el bucle principal:
   ```powershell
   python pasarrato.py
   ```

---

## 🎵 Créditos y Atribución (Fair Use)

La identidad sonora de este proyecto utiliza *assets* con fines estrictamente educativos y no comerciales, bajo el principio de *Fair Use*. Los derechos de propiedad intelectual de todos los sonidos y temas musicales incluidos en este proyecto pertenecen a su autor/empresa:
*   **Toby Fox** (Efectos y temas de *Undertale*).
*   **Phoenix Network** (Música del menú de *Galaxy Life*).
*   **Riot Games** (Voces y efectos de *League of Legends*).

*Si eres el propietario de estos derechos y deseas que se eliminen los sonidos de este proyecto, por favor, contacta conmigo a maximus.jasso@gmail.com y procederé a eliminarlos.*

Ultima modificación: Septiembre - 2026
