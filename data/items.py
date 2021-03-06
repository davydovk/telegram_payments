from dataclasses import dataclass


@dataclass
class Item:
    id: int
    title: str
    description: str
    price: int
    photo_link: str


F_Line_33 = Item(
    id=1,
    title='F-Line 33',
    description="""
<b>F-Line 33</b> — яхта для тех, кто не изменяет своему стилю ни на воде, ни на суше.
Эксклюзивный корпус F-Line 33 (017) готов к вашим путешествиям летом 2021 года и 
может быть доставлен в любую точку России или Европы.

Комплектация F-Line 33 (017):
Корпус серого цвета c отделкой интерьера дубом песочного цвета, салон светло-серый. 
Кондиционер, барная стойка в кокпите, гидравлический откидной борт в транце, носовое 
подруливающее устройство, генератор для бензиновых двигателей – Westerbeke 3.5W и многое другое. 
Полная комплектация с мощными бензиновыми двигателями 2 x Volvo V8 430 CE/DPS, 860 л.с., 
максимальная скорость 45 узлов.
""",
    price=10,
    photo_link=r'https://fairline-russia.com/uploads/2021/05/17-52-44_20210524_2b3a8606.jpg'
)

Targa_43_Open = Item(
    id=2,
    title='Targa 43 Open',
    description="""
<b>Targa 43 Open</b> — Круизная яхта Targa 43 Open, одна из самых успешных моделей в хардтопной линейке Fairline, 
создана всемирно известным дизайнером суперъяхт Альберто Манчини. Премьера состоялась осенью 
2018 года на яхтенной выставке в Каннах, где яхта сразу была признана победительницей World Yachts Trophies 
в категории «Лучший дизайн экстерьера яхты 14-18м».

Яхта имеет просторные каюты, качественную и дорогую отделку, характерную для британского бренда Fairline. 
Мастер-каюта во всю ширину корпуса находится на миделе и имеет высокий потолок «во весь рост» и пол в один 
уровень. Верхний салон дополнительно укомплектован системой Webasto. Гараж вмещает тендер или гидроцикл 
до 2,8 м + остается место для хранения других водных игрушек.
""",
    price=200,
    photo_link=r'https://fairline-russia.com/uploads/2021/04/fairline-targa-43-exterior1-800x534@2x.jpg'
)

Princess_58 = Item(
    id=3,
    title='Princess 58',
    description="""
<b>Princess 58</b> — Яхта Princess 58 с флайбриджем. Построена на британской верфи в 2008 году. 
Три каюты для шести персон. Мастер-кабина во всю ширину корпуса.
Две душевые комнаты для vip и мастер-кают. Ухоженный салон и все палубное оборудование.
На яхте установлены гидравлический трап и носовое подруливающее устройство.
""",
    price=100,
    photo_link=r'https://fairline-russia.com/uploads/2020/10/princess-58.jpg'
)

items = (
    F_Line_33, Targa_43_Open, Princess_58
)
