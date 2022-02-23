from django.contrib import admin

# Register your models here.
from kursach.models import *


@admin.register(Mode)
class ModeAdmin(admin.ModelAdmin):
    pass


@admin.register(Biom)
class BiomAdmin(admin.ModelAdmin):
    pass


@admin.register(Craft)
class CraftAdmin(admin.ModelAdmin):
    pass


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass


@admin.register(Seed)
class SeedAdmin(admin.ModelAdmin):
    pass


@admin.register(Plants)
class PlantsAdmin(admin.ModelAdmin):
    pass


@admin.register(CraftIngredient)
class CraftIngredientAdmin(admin.ModelAdmin):
    pass


@admin.register(Accessory)
class AccessoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Effect)
class EffectAdmin(admin.ModelAdmin):
    pass


@admin.register(Elixir)
class ElixirAdmin(admin.ModelAdmin):
    pass


@admin.register(WeaponType)
class WeaponTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    pass


@admin.register(WeaponDamage)
class WeaponDamageAdmin(admin.ModelAdmin):
    pass


@admin.register(Fish)
class FishAdmin(admin.ModelAdmin):
    pass


@admin.register(FishBiom)
class FishBiomAdmin(admin.ModelAdmin):
    pass


@admin.register(Monster)
class MonsterAdmin(admin.ModelAdmin):
    pass


@admin.register(MonsterBiom)
class MonsterBiomAdmin(admin.ModelAdmin):
    pass


@admin.register(MonsterHp)
class MonsterHpAdmin(admin.ModelAdmin):
    pass


@admin.register(Boss)
class BossAdmin(admin.ModelAdmin):
    pass


@admin.register(BossHp)
class BossHpAdmin(admin.ModelAdmin):
    pass


@admin.register(CharClass)
class CharClassAdmin(admin.ModelAdmin):
    pass


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    pass


@admin.register(FishQuest)
class FishQuestAdmin(admin.ModelAdmin):
    pass


@admin.register(BossQuest)
class BossQuestAdmin(admin.ModelAdmin):
    pass


@admin.register(Armour)
class ArmourAdmin(admin.ModelAdmin):
    pass
