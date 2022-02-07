"""Тестовое задание для Радиум на позицию стажёр-программист Python."""
import asyncio
import hashlib
from secrets import randbelow


async def test_task_printer(text, rand):
    await asyncio.sleep(rand)
    print(text)


my_data = [
    asyncio.ensure_future(test_task_printer('Роман', randbelow(5))),
    asyncio.ensure_future(test_task_printer('Стажёр-программист Python', randbelow(5))),
    asyncio.ensure_future(test_task_printer('40.000 рублей', randbelow(5))),
]

event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(asyncio.gather(*my_data))
event_loop.close()

user_string = input('Запрос данных от пользователя: ')
hash_string = hashlib.sha256(user_string.encode('utf-8')).hexdigest()
print('SHA-256 hash:', hash_string)
