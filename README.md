### Podstawowy adres: `/api/v1`

## 🧙 HERO STATS

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

```json
Request:
{
  "level": int
}

Response:
{
  "exp_amount": float
}
```

---

### POST `/hero-stats/experience`

**Obliczanie doświadczenia pozyskiwanego z potworów**

```json
Request:
{
  "player_level": int,
  "npc_level": int
}

Response:
{
  "experience": float
}
```

---

### POST `/hero-stats/experience-penalty`

**Obliczanie redukcji doświadczenia (%)**

```json
Request:
{
  "player_level": int,
  "npc_level": int
}

Response:
{
  "experience_penalty": float
}
```

---

### POST `/hero-stats/highest-level`

**Obliczanie najwyższego poziomu w grupie**

```json
Request:
{
  "server_factor": float,
  "level_ally_min": int
}

Response:
{
  "max_level": int
}
```

---

### POST `/hero-stats/strength`

**Obliczanie statystyk zależnych od siły**

```json
Request:
{
  "strength": int,
  "armor_level": int,
  "level": int
}

Response:
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

```json
Request:
{
  "intellect": int,
  "level": int
}

Response:
{
  "absorb_limit": float,
  "crit_value_gain": float
}
```

---

### POST `/hero-stats/dexterity`

**Obliczanie statystyk zależnych od zręczności**

```json
Request:
{
  "dexterity": int
}

Response:
{
  "attack_speed": float,
  "evade_gain": float
}
```

---

### POST `/hero-stats/evade`

**Obliczanie szansy na unik (%)**

```json
Request:
{
  "evade": float,
  "enemy_level": int
}

Response:
{
  "evade_percentage": float
}
```

---

### POST `/hero-stats/block`

**Obliczanie szansy na blok (%)**

```json
Request:
{
  "block": float,
  "enemy_level": int
}

Response:
{
  "block_percentage": float
}
```

---

## ⚔️ ITEM STATS

### POST `/item-stats/item-power`

**Obliczanie współczynników rzadkości i poziomu przedmiotu**

```json
Request:
{
  "level": int,
  "rarity_factor": float
}

Response:
{
  "item_level_power": float,
  "item_rarity_power": float
}
```

---

### POST `/item-stats/weapon-damage`

**Obliczanie wartości obrażeń broni**

```json
Request:
{
  "weapon_factor": float,
  "item_rarity_power": float,
  "item_level_power": float,
  "item_damage_spread": float
}

Response:
{
  "item_damage": float,
  "item_damage_top": float,
  "item_damage_bottom": float
}
```

---

### POST `/item-stats/weapon-slow`

**Obliczanie wartości spowolnienia broni**

```json
Request:
{
  "slow_factor": float,
  "item_level": int
}

Response:
{
  "item_slow": float
}
```

---

### POST `/item-stats/*-damage-reduction`

**Obliczanie wartości redukcji obrażeń**

* - (physical, range, secondary, fire, frost, light)

```json
Request:
{
  "damage_in": float,
  "armor": float
}

Response:
{
  "damage_out": float
}
```

---

### POST `/item-stats/crit-chance-gain`

**Obliczanie wartości wzrostu szansy na cios krytyczny (%)**

```json
Request:
{
  "player_level": int,
  "enemy_level": int
}

Response:
{
  "crit_chance_gain": float
}
```

---

### POST `/item-stats/crit-power-gain`

**Obliczanie wartości wzrostu mocy ciosu krytycznego**

```json
Request:
{
  "player_level": int,
  "enemy_level": int
}

Response:
{
  "crit_power_gain": float
}
```

---

### POST `/item-stats/item-armor`

**Obliczanie wartości pancerza przedmiotu**

```json
Request:
{
  "armor_factor": float,
  "class_power": float,
  "rarity_power": float,
  "level_power": float
}

Response:
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

---

## ✨ LEGENDARY BONUS

### POST `/legendary-bonus/expiration`

**Obliczanie poziomu osłabienia i wygaśnięcia bonusu legendarnego**

```json
Request:
{
  "item_level": int
}

Response:
{
  "first_nerf_level": int,
  "expiration_level": int
}
```

---

### GET endpoints

| Endpoint                             | Opis       |
| ------------------------------------ | ------------------- |
| `/legendary-bonus/bonuses` | Lista wszystkich bonusów legendarnych |

---

### POST `/legendary-bonus/very-crit`

**Obliczanie szansy i mocy ciosu bardzo krytycznego**

```json
Request:
{
  "crit_chance": float,
  "crit_power": float
}

Response:
{
  "very_crit_chance": float,
  "very_crit_power": float
}
```

---

### POST `/legendary-bonus/holy-touch`

**Obliczanie wartości leczenia dotyku anioła**

```json
Request:
{
  "hp": float
}

Response:
{
  "healing_per_round": float,
  "rounds": int,
  "total_healing": float
}
```

---

### POST `/legendary-bonus/anguish`

**Obliczanie wartości obrażeń krwawej udręki**

```json
Request:
{
  "level": int,
  "strength": int,
  "intellect": int,
  "agility": int
}

Response:
{
  "damage": float
}
```

