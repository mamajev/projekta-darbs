# Space Invaders Spēles Dokumentācija
(C)Dmitrijs Mamajevs
Šī dokumentācija izskaidro Python kodu, kas izveidots Space Invaders spēlei, izmantojot Pygame bibliotēku.

## Failu struktūra
Spēles failu struktūra ir šāda:

```
.
├── assets
│   ├── background.jpg
│   ├── boss.png
│   ├── bullet.png
│   ├── enemy.png
│   ├── phantomstorm.ttf
│   ├── player.png
│   └── skerslis.png
└── main.py
```

- "main.py" ir galvenais Python failu, kurā ir visa spēles koda loģika.
- "assets" mapē ir visi attēlu un fontu faili, ko izmanto spēlē.

## Koda Paskaidrojumi

```python
import pygame
import os
import random
```

Importējam nepieciešamās bibliotēkas: Pygame spēles izstrādei, OS failu darbībām un Random gadījuma skaitļu ģenerēšanai.

```python
def game_over_menu(score):
```
Funkcija, kas tiek izsaukta, kad spēlētājs zaudē. Parāda "Game Over" menu, kurā redzams sasniegtais punktu skaits un iespēja atkārtoti spēlēt vai iziet no spēles.

```python
def draw_text(surface, text, x, y, font):
```
Funkcija, kas attēlo tekstu uz ekrāna noteiktā koordinātā.

```python
pygame.init()
```
Inicializējam Pygame.

```python
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")
```
Definējam spēles loga izmērus un nosaukumu.

```python
player_img = pygame.image.load(os.path.join('assets', 'player.png'))
```
Ielādējam spēlē izmantotos attēlus, izmantojot attiecīgos ceļus.

```python
class Player(pygame.sprite.Sprite):
```
Definējam Spēlētāja klasi, kas manto Pygame Sprite klasi. Šī klase satur informāciju par spēlētāju un metodes tā atjaunināšanai.

```python
class Enemy(pygame.sprite.Sprite):
```
Definējam Ienaidnieka klasi, kas manto Pygame Sprite klasi. Šī klase satur informāciju par ienaidniekiem un metodes to atjaunināšanai.

```python
class Boss(pygame.sprite.Sprite):
```
Definējam Boss klasi, kas manto Pygame Sprite klasi. Šī klase satur informāciju par boss un metodes tā atjaunināšanai.

```python
class Bullet(pygame.sprite.Sprite):
```
Definējam Lodes klasi, kas manto Pygame Sprite klasi. Šī klase satur informāciju par lodēm un metodes to atjaunināšanai.

```python
def main():
```
Šī funkcija ir spēles galvenā cilpa, kas kontrolē visu spēles darbību. Tā ietver spēles stāvokļa atjaunināšanu, notikumu apstrādi un zīmēšanu ekrānā.

```python
clock = pygame.time.Clock()
```
Izveidojam pulksteni, lai kontrolētu spēles kadru ātrumu.

```python
run = True
while run:
```
Galvenā spēles cilpa turpināsies, kamēr `run` ir `True`.

```python
clock.tick(FPS)
```
Ierobežojam spēles kadru ātrumu ar iepriekš definēto FPS vērtību.

```python
for event in pygame.event.get():
```
Apstrādājam visus notikumus, kas notiek spēlē.

```python
keys = pygame.key.get_pressed()
```
Iegūstam informāciju par visām nospiedtajām taustiņiem.

```python
player.update(keys)
```
Atjauninām spēlētāja stāvokli, balstoties uz nospiedtajām taustiņām.

```python
enemies.update()
```
Atjauninām ienaidnieku stāvokli.

```python
bullets.update()
```
Atjauninām ložu stāvokli.

```python
pygame.display.flip()
```
Atjauninām ekrāna attēlojumu, lai redzētu visus veiktos zīmējumus un atjauninājumus.

```python
pygame.quit()
```
Beidzam Pygame sesiju, kad spēle tiek aizvērta.

## Koda palaišana
Lai palaistu kodu, jums ir nepieciešams Python vides izpildlaiks, kurā ir instalēta Pygame bibliotēka. Palaistu kodu, atveriet terminālu vai komandrindu un ierakstiet:

```shell
python main.py
```

```python
if __name__ == "__main__":
    main()
```

Šis kods nodrošina, ka spēles galvenā cilpa tiks izsaukta tikai tad, ja šis skripts tiek izpildīts kā galvenais faila. Ja to importē kā moduli citā skriptā, galvenā cilpa netiks izsaukta.

# Koda struktūra

Šis kods ir strukturēts sekojoši:

- Importa sadaļa
- Definējumi un globālas konstantes
- Spēles klases
- Spēles funkcijas
- Galvenā spēles cilpa

Katrs no šiem blokiem ir svarīgs spēles darbībai un tie ir izvietoti šādā secībā, lai nodrošinātu pareizu atkarību izpildi. Piemēram, klases ir definētas pirms galvenās spēles cilpas, lai tās būtu pieejamas cilpas iekšienē.

Visbeidzot, ir svarīgi atzīmēt, ka šis kods ir rakstīts, izmantojot Python 3 un Pygame bibliotēku. Python ir populāra programmēšanas valoda datu zinātnē, mākslīgajā intelektā un citās jomās, un Pygame ir vienkārša, bet spējīga 2D spēļu izstrādes bibliotēka Python valodā.
