# 3)	Создайте класс Soda (для определения типа газированной воды), принимающий 1 аргумент при инициализации
# (отвечающий за добавку к выбираемому лимонаду). В этом классе реализуйте метод show_my_drink(), выводящий на печать
# «Газировка и {ДОБАВКА}» в случае наличия добавки, а иначе отобразится следующая фраза: «Обычная газировка».


class Soda:
    def __init__(self, ingredients = None):
           self.ingredients = ingredients



    def show_my_drink(self):
        if self.ingredients:
            print(f'Газированная вода {self.ingredients}')
        else:
            print('Простая петьевая вода!')

water1 = Soda('Апельсин')
water2 = Soda('Кислота')
water3 = Soda()
water1.show_my_drink()
water2.show_my_drink()
water3.show_my_drink()










