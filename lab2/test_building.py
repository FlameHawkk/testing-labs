"""
Модульные тесты для класса Building.
Запуск:  python test_building.py
"""

import unittest
from building import Building

class TestBuilding(unittest.TestCase):

    # --- Проверка из условия задачи ---
    def test_example_from_task(self):
        # M=6, N=6 → 36 + 66 = 102
        b = Building(6, 6)
        self.assertEqual(b.total_panels, 102)

    # --- Только крыша (M=0) ---
    def test_only_roof(self):
        b = Building(0, 5)
        self.assertEqual(b.roof_panels, 25)
        self.assertEqual(b.base_panels, 0)
        self.assertEqual(b.total_panels, 25)

    # --- Только основание + одна панель крыши ---
    def test_minimal_roof(self):
        # N=1 → крыша 1 панель, ширина основания 1
        b = Building(5, 1)
        self.assertEqual(b.roof_panels, 1)
        self.assertEqual(b.base_panels, 5)
        self.assertEqual(b.total_panels, 6)

    # --- Граница: M=0, N=1 ---
    def test_edge_m0_n1(self):
        b = Building(0, 1)
        self.assertEqual(b.total_panels, 1)

    # --- Большие значения ---
    def test_big_values(self):
        M, N = 10**9, 10**9
        b = Building(M, N)
        expected = N * N + M * (2 * N - 1)
        self.assertEqual(b.total_panels, expected)

    # --- Валидация ввода ---
    def test_negative_m_raises(self):
        with self.assertRaises(ValueError):
            Building(-1, 5)

    def test_zero_n_raises(self):
        with self.assertRaises(ValueError):
            Building(5, 0)

    def test_negative_n_raises(self):
        with self.assertRaises(ValueError):
            Building(5, -3)

    def test_float_m_raises(self):
        with self.assertRaises(TypeError):
            Building(2.5, 5)

    # --- Независимость крыши от M и наоборот ---
    def test_roof_independent_of_m(self):
        a = Building(1, 7)
        b = Building(100, 7)
        self.assertEqual(a.roof_panels, b.roof_panels)

    def test_base_proportional_to_m(self):
        # При одинаковом N основание пропорционально M
        a = Building(2, 5)
        b = Building(4, 5)
        self.assertEqual(b.base_panels, 2 * a.base_panels)


if __name__ == "__main__":
    unittest.main(verbosity=2)