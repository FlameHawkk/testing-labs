"""
Класс Building — расчёт количества панелей для здания.
Крыша: N рядов, треугольник, всего N² панелей.
Основание: M рядов, ширина 2N−1, всего M*(2N−1) панелей.
"""

class Building:
    def __init__(self, M, N):
        """
        M — высота основания (0 ≤ M ≤ 10⁹)
        N — высота крыши      (1 ≤ N ≤ 10⁹)
        """
        if not isinstance(M, int) or not isinstance(N, int):
            raise TypeError("M и N должны быть целыми числами")
        if M < 0:
            raise ValueError("M не может быть отрицательным")
        if N < 1:
            raise ValueError("N должно быть не меньше 1")
        self.M = M
        self.N = N

    @property
    def roof_panels(self):
        """Крыша: N рядов, сумма 1+3+…+(2N−1) = N²."""
        return self.N * self.N

    @property
    def base_panels(self):
        """Основание: M рядов по (2N−1) панелей."""
        return self.M * (2 * self.N - 1)

    @property
    def total_panels(self):
        """Всего панелей."""
        return self.roof_panels + self.base_panels

    def __repr__(self):
        return f"Building(M={self.M}, N={self.N}, total={self.total_panels})"