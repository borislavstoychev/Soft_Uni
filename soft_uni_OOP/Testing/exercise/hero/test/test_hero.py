from project.hero import Hero

import unittest


class HeroTest(unittest.TestCase):

    def setUp(self) -> None:
        self.hero = Hero("Bobby", 25, 98, 2)

    def test_constructor(self):
        self.assertEqual("Bobby", self.hero.username)
        self.assertEqual(25, self.hero.level)
        self.assertEqual(98, self.hero.health)
        self.assertEqual(2, self.hero.damage)

    def test_enemy_hero_and_hero_are_equal(self):
        with self.assertRaises(Exception):
            enemy_hero = Hero("Bobby", 25, 98, 2)
            self.hero.battle(enemy_hero)

    def test_battle_hero_health_less_than_zro(self):
        enemy_hero = Hero("Borko", 25, 98, 2)
        self.hero.health = 0
        with self.assertRaises(Exception):
            self.hero.battle(enemy_hero)

    def test_battle_enemy_health_less_than_zro(self):
        enemy_hero = Hero("Borko", 25, 0, 2)
        with self.assertRaises(Exception):
            self.hero.battle(enemy_hero)

    def test_player_health_when_payer_loss(self):
        enemy_hero = Hero("Borko", 25, 75, 2)
        self.assertEqual("You lose", self.hero.battle(enemy_hero) )
        self.assertEqual(48, self.hero.health)
        self.assertEqual(30, enemy_hero.health)
        self.assertEqual(26, enemy_hero.level)
        self.assertEqual(7, enemy_hero.damage)

    def test_player_health_if_payer_win(self):
        enemy_hero = Hero("Borko", 25, 50, 2)
        self.assertEqual("You win", self.hero.battle(enemy_hero))
        self.assertEqual(53, self.hero.health)
        self.assertEqual(0, enemy_hero.health)
        self.assertEqual(26, self.hero.level)
        self.assertEqual(7, self.hero.damage)

    def test_if_hero_and_enemy_are_equal_to_zero(self):
        enemy_hero = Hero("Borko", 49, 50, 2)
        self.assertEqual("Draw", self.hero.battle(enemy_hero))

    def test_repr_hero(self):
        expect = f"Hero Bobby: 25 lvl\nHealth: 98\nDamage: 2\n"
        self.assertEqual(expect, self.hero.__str__())


if __name__ == "__main__":
    unittest.main()