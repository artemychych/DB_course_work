from django.db import models


class Mode(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "mode"


class Biom(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "biom"


class Craft(models.Model):
    id = models.BigIntegerField(primary_key=True)
    description = models.TextField()

    class Meta:
        db_table = "craft"


class Ingredient(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    cost = models.IntegerField()

    class Meta:
        db_table = "ingredient"


class Seed(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    biom_id = models.ForeignKey('Biom', on_delete=models.PROTECT,)

    class Meta:
        db_table = "seed"


class Plants(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    seed_id = models.ForeignKey('Seed', on_delete=models.PROTECT,)
    ingredient = models.ForeignKey('Ingredient', on_delete=models.PROTECT,)

    class Meta:
        db_table = "plants"


class CraftIngredient(models.Model):
    id = models.BigIntegerField(primary_key=True)
    ingredient_id = models.ForeignKey('Ingredient', on_delete=models.PROTECT)
    craft_id = models.ForeignKey('Craft', on_delete=models.PROTECT,)

    class Meta:
        db_table = "craft_ingredient"


class Accessory(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    craft_id = models.ForeignKey('Craft', on_delete=models.PROTECT,)

    class Meta:
        db_table = "accessory"


class Effect(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        db_table = "effect"


class Elixir(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    cost = models.SmallIntegerField()
    effect_id = models.ForeignKey('Effect', on_delete=models.PROTECT)
    craft_id = models.ForeignKey('Craft', on_delete=models.PROTECT, )

    class Meta:
        db_table = "elixir"


class WeaponType(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "weapon_type"


class Weapon(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    type_id = models.ForeignKey('WeaponType', on_delete=models.PROTECT)
    attack_speed = models.SmallIntegerField()
    craft_id = models.ForeignKey('Craft', on_delete=models.PROTECT, )

    class Meta:
        db_table = "weapon"


class WeaponDamage(models.Model):
    id = models.BigIntegerField(primary_key=True)
    weapon_id = models.ForeignKey('Weapon', on_delete=models.PROTECT)
    mode_id = models.ForeignKey('Mode', on_delete=models.PROTECT, )
    damage = models.SmallIntegerField()

    class Meta:
        db_table = "weapon_damage"


class Fish(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    cost = models.SmallIntegerField()

    class Meta:
        db_table = "fish"


class FishBiom(models.Model):
    id = models.BigIntegerField(primary_key=True)
    fish_id = models.ForeignKey('Fish', on_delete=models.PROTECT)
    biom_id = models.ForeignKey('Biom', on_delete=models.PROTECT, )

    class Meta:
        db_table = "fish_biom"


class Monster(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    armor = models.SmallIntegerField()
    damage = models.SmallIntegerField()

    class Meta:
        db_table = "monster"


class MonsterBiom(models.Model):
    id = models.BigIntegerField(primary_key=True)
    monster_id = models.ForeignKey('Monster', on_delete=models.PROTECT)
    biom_id = models.ForeignKey('Biom', on_delete=models.PROTECT, )

    class Meta:
        db_table = "monster_biom"


class MonsterHp(models.Model):
    id = models.BigIntegerField(primary_key=True)
    monster_id = models.ForeignKey('Monster', on_delete=models.PROTECT)
    mode_id = models.ForeignKey('Mode', on_delete=models.PROTECT)
    hp = models.SmallIntegerField()

    class Meta:
        db_table = "monster_hp"


class Boss(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    armor = models.SmallIntegerField()
    damage = models.SmallIntegerField()
    trophy_name = models.CharField(max_length=100)
    biom_id = models.ForeignKey('Biom', on_delete=models.PROTECT, )

    class Meta:
        db_table = "boss"


class BossHp(models.Model):
    id = models.BigIntegerField(primary_key=True)
    monster_id = models.ForeignKey('Boss', on_delete=models.PROTECT)
    mode_id = models.ForeignKey('Mode', on_delete=models.PROTECT)
    hp = models.SmallIntegerField()

    class Meta:
        db_table = "boss_hp"


class CharClass(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "char_class"


class Character(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    hp = models.SmallIntegerField()
    mana = models.SmallIntegerField()
    armor = models.SmallIntegerField()
    speed = models.SmallIntegerField()
    hp_regen = models.SmallIntegerField()
    block_speed = models.SmallIntegerField()
    char_class_id = models.ForeignKey('CharClass', on_delete=models.PROTECT)

    class Meta:
        db_table = "character"


class FishQuest(models.Model):
    id = models.BigIntegerField(primary_key=True)
    fish_id = models.ForeignKey('Fish', on_delete=models.PROTECT)
    character_id = models.ForeignKey('Character', on_delete=models.PROTECT)
    reward = models.SmallIntegerField()

    class Meta:
        db_table = "fish_quest"


class BossQuest(models.Model):
    id = models.BigIntegerField(primary_key=True)
    boss_id = models.ForeignKey('Boss', on_delete=models.PROTECT)
    character_id = models.ForeignKey('Character', on_delete=models.PROTECT)
    reward = models.SmallIntegerField()

    class Meta:
        db_table = "boss_quest"


class Armour(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    armor = models.SmallIntegerField()
    char_class_id = models.ForeignKey('CharClass', on_delete=models.PROTECT)
    craft_id = models.ForeignKey('Craft', on_delete=models.PROTECT)

    class Meta:
        db_table = "armour"
