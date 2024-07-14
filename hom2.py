import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    # Регулярний вираз для пошуку дійсних чисел, відокремлених пробілами
    pattern = r'(?<!\S)-?\d+(?:\.\d+)?(?!\S)'
    for match in re.findall(pattern, text):
        yield float(match)

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    return sum(func(text))

# Основний блок
if __name__ == "__main__":
    text = input("Введіть текст: ")
    numbers = list(generator_numbers(text))
    total_profit = sum_profit(text, generator_numbers)

    print("Знайдені числа:", numbers)
    print("Загальна сума чисел:", total_profit)


