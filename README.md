***Dane do realizacji projektu pochodzą z [Mechaniki Gry Margonem](https://pomoc.margonem.pl/index/view,372)***

## Spis treści

- [Podstawowy adres](#podstawowy-adres)
- [🧙 Statystyki bohatera (HERO STATS)](#-statystyki-bohatera-hero-stats)
  - [POST `/hero-stats/base-stats`](#post-hero-statsbase-stats)
  - [POST `/hero-stats/exp-amount`](#post-hero-statsexp-amount)
  - [POST `/hero-stats/experience`](#post-hero-statsexperience)
  - [POST `/hero-stats/experience-penalty`](#post-hero-statsexperience-penalty)
  - [POST `/hero-stats/highest-level`](#post-hero-statshighest-level)
  - [POST `/hero-stats/strength`](#post-hero-statsstrength)
  - [POST `/hero-stats/intellect`](#post-hero-statsintellect)
  - [POST `/hero-stats/dexterity`](#post-hero-statsdexterity)
  - [POST `/hero-stats/evade`](#post-hero-statsevade)
  - [POST `/hero-stats/block`](#post-hero-statsblock)

- [⚔️ Statystyki przedmiotów (ITEM STATS)](#-statystyki-przedmiotow-item-stats)
  - [POST `/item-stats/item-power`](#post-item-statsitem-power)
  - [POST `/item-stats/weapon-damage`](#post-item-statsweapon-damage)
  - [POST `/item-stats/weapon-slow`](#post-item-statsweapon-slow)
  - [POST `/item-stats/*-damage-reduction`](#post-item-stats--damage-reduction)
  - [POST `/item-stats/crit-chance-gain`](#post-item-statscrit-chance-gain)
  - [POST `/item-stats/crit-power-gain`](#post-item-statscrit-power-gain)
  - [POST `/item-stats/item-armor`](#post-item-statsitem-armor)
  - [POST `/item-stats/item-stats`](#post-item-statsitem-stats)
  - [GET endpoints](#get-endpoints)

- [✨ Bonusy Legendarne (LEGENDARY BONUSES)](#-bonusy-legendarne-legendary-bonuses)
  - [POST `/legendary-bonus/expiration`](#post-legendary-bonusexpiration)
  - [POST `/legendary-bonus/very-crit`](#post-legendary-bonusvery-crit)
  - [POST `/legendary-bonus/holy-touch`](#post-legendary-bonusholy-touch)
  - [POST `/legendary-bonus/anguish`](#post-legendary-bonusanguish)
  - [GET endpoints](#get-endpoints-1)

## Podstawowy adres

`/api/v1`

## 🧙 Statystyki bohatera (HERO STATS)

### POST `/hero-stats/base-stats`

**Obliczanie podstawowej wartości HP oraz szansy na cios krytyczny**

**Request**

```json
{
  "level": int
}
```

**Response**

```json
{
  "base_hp": float,
  "base_crit_value": float
}
```

---

### POST `/hero-stats/exp-amount`

**Obliczanie ilości doświadczenia potrzebnego do awansu na kolejny poziom**

**Request**

```json
{
  "level": int
}
```

**Response**

```json
{
  "exp_amount": float
}
```

---

### POST `/hero-stats/experience`

**Obliczanie doświadczenia pozyskiwanego z potworów**

**Request**

```json
{
  "player_level": int,
  "npc_level": int
}
```

**Response**

```json
{
  "experience": float
}
```

---

### POST `/hero-stats/experience-penalty`

**Obliczanie redukcji doświadczenia (%)**

**Request**

```json
{
  "player_level": int,
  "npc_level": int
}
```

**Response**

```json
{
  "experience_penalty": float
}
```

---

### POST `/hero-stats/highest-level`

**Obliczanie najwyższego poziomu w grupie**

**Request**

```json
{
  "server_factor": float,
  "level_ally_min": int
}
```

**Response**

```json
{
  "max_level": int
}
```

---

### POST `/hero-stats/strength`

**Obliczanie statystyk zależnych od siły**

**Request**

```json
{
  "strength": int,
  "armor_level": int,
  "level": int
}
```

**Response**

```json
{
  "base_hp_gain": float,
  "armor_hp_gain": float,
  "total_hp_gain": float,
  "crit_value_gain": float
}
```

---

### POST `/hero-stats/intellect`

**Obliczanie statystyk zależnych od intelektu**

**Request**

```json
{
  "intellect": int,
  "level": int
}
```

**Response**

```json
{
  "absorb_limit": float,
  "crit_value_gain": float
}
```

---

### POST `/hero-stats/dexterity`

**Obliczanie statystyk zależnych od zręczności**

**Request**

```json
{
  "dexterity": int
}
```

**Response**

```json
{
  "attack_speed": float,
  "evade_gain": float
}
```

---

### POST `/hero-stats/evade`

**Obliczanie szansy na unik (%)**

**Request**

```json
{
  "evade": float,
  "enemy_level": int
}
```

**Response**

```json
{
  "evade_percentage": float
}
```

---

### POST `/hero-stats/block`

**Obliczanie szansy na blok (%)**

**Request**

```json
{
  "block": float,
  "enemy_level": int
}
```

**Response**

```json
{
  "block_percentage": float
}
```

---

## ⚔️ Statystyki przedmiotów (ITEM STATS)

### POST `/item-stats/item-power`

**Obliczanie współczynników rzadkości i poziomu przedmiotu**

**Request**

```json
{
  "level": int,
  "rarity_factor": float
}
```

**Response**

```json
{
  "item_level_power": float,
  "item_rarity_power": float
}
```

---

### POST `/item-stats/weapon-damage`

**Obliczanie wartości obrażeń broni**

**Request**

```json
{
  "weapon_factor": float,
  "item_rarity_power": float,
  "item_level_power": float,
  "item_damage_spread": float
}
```

**Response**

```json
{
  "item_damage": float,
  "item_damage_top": float,
  "item_damage_bottom": float
}
```

---

### POST `/item-stats/weapon-slow`

**Obliczanie wartości spowolnienia broni**

**Request**

```json
{
  "slow_factor": float,
  "item_level": int
}
```

**Response**

```json
{
  "item_slow": float
}
```

---

### POST `/item-stats/*-damage-reduction`

**Obliczanie wartości redukcji obrażeń**

* - (physical, range, secondary, fire, frost, light)

**Request**

```json
{
  "damage_in": float,
  "armor": float
}
```

**Response**

```json
{
  "damage_out": float
}
```

---

### POST `/item-stats/crit-chance-gain`

**Obliczanie wartości wzrostu szansy na cios krytyczny (%)**

**Request**

```json
{
  "player_level": int,
  "enemy_level": int
}
```

**Response**

```json
{
  "crit_chance_gain": float
}
```

---

### POST `/item-stats/crit-power-gain`

**Obliczanie wartości wzrostu mocy ciosu krytycznego**

**Request**

```json
{
  "player_level": int,
  "enemy_level": int
}
```

**Response**

```json
{
  "crit_power_gain": float
}
```

---

### POST `/item-stats/item-armor`

**Obliczanie wartości pancerza przedmiotu**

**Request**

```json
{
  "armor_factor": float,
  "class_power": float,
  "rarity_power": float,
  "level_power": float
}
```

**Response**

```json
{
  "armor": float
}
```

---

### POST `/item-stats/item-stats`

**Obliczanie wartości wszystkich cech**


---

### GET endpoints

| Endpoint                             | Opis         |
| ------------------------------------ | ------------------- |
| `/item-stats/bless-legendary-chance` | Szanse na przedmiot legendarny z błogosławieństwem   |
| `/item-stats/item-rarity-amount`     | Ilośc przedmiotów w szablonie dla poszczególnych typów potworów |
| `/item-stats/item-loot-chance`       | Szanse na przedmioty dla poszczególnych typów potworów         |
| `/item-stats/item-bonus-amount`      | Ilość bonusów w przedmiotach         |
| `/item-stats/item-class-power`       | Mnożniki mocy dla poszczególnych typów przedmiotów   |
| `/item-stats/weapon-factor`       | Współczynnik obrażeń broni   |
| `/item-stats/slow-factor`       | Współczynnik spowolnienia broni   |
| `/item-stats/item-manual-bonuses`       | Lista bonusów w przedmiotach nadawana manualnie  |
| `/item-stats/item-actions`       | Lista dostępnych akcji przedmiotów  |

---

## ✨ Bonusy Legendarne (LEGENDARY BONUSES)

### POST `/legendary-bonus/expiration`

**Obliczanie poziomu osłabienia i wygaśnięcia bonusu legendarnego**

**Request**

```json
{
  "item_level": int
}
```

**Response**

```json
{
  "first_nerf_level": int,
  "expiration_level": int
}
```

### POST `/legendary-bonus/very-crit`

**Obliczanie szansy i mocy ciosu bardzo krytycznego**

**Request**

```json
{
  "crit_chance": float,
  "crit_power": float
}
```

**Response**

```json
{
  "very_crit_chance": float,
  "very_crit_power": float
}
```

---

### POST `/legendary-bonus/holy-touch`

**Obliczanie wartości leczenia dotyku anioła**

**Request**

```json
{
  "hp": float
}
```

**Response**

```json
{
  "healing_per_round": float,
  "rounds": int,
  "total_healing": float
}
```

---

### POST `/legendary-bonus/anguish`

**Obliczanie wartości obrażeń krwawej udręki**

**Request**

```json
{
  "level": int,
  "strength": int,
  "intellect": int,
  "agility": int
}
```

**Response**

```json
{
  "damage": float
}
```
---

### GET endpoints

| Endpoint                             | Opis       |
| ------------------------------------ | ------------------- |
| `/legendary-bonus/bonuses` | Lista wszystkich bonusów legendarnych |

---
