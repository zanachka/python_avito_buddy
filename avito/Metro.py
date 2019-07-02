from enum import Enum, unique


@unique
class SpbMetro(Enum):
    PROSPECT_VETERANOV = ('Проспект Ветеранов', 59.84188, 30.251543)
    LENINSKIY_PROSPECT = ('Ленинский проспект', 59.851677, 30.268279)
    AVTOVO = ('Автово', 59.867369, 30.261345)
    KIROVSKIY_ZAVOD = ('Кировский завод', 59.879726, 30.261908)
    NARVSKAYA = ('Нарвская', 59.901169, 30.274676)
    BALTIYSKAJA = ('Балтийская', 59.907245, 30.299217)
    TECHNOLOGICHESKIY_INSTITUT_1 = ('Технологический институт-1', 59.916799, 30.318967)
    PUSHKINSKAJA = ('Пушкинская', 59.920757, 30.329641)
    VLADIMIRSKAJA = ('Владимирская', 59.927467, 30.347875)
    PLOSHAD_VOSSTANIJA = ('Площадь Восстания', 59.931483, 30.36036)
    CHERNISHEVSKAJA = ('Чернышевская', 59.944558, 30.359754)
    PLOSHAD_LENINA = ('Площадь Ленина', 59.955725, 30.355957)
    VIBORRGSKAJA = ('Выборгская', 59.97111, 30.347553)
    LESNAJA = ('Лесная', 59.98477, 30.344201)
    PLOSHAD_MUZHESTVA = ('Площадь Мужества', 59.999655, 30.366595)
    POLITECHNICHESKAJA = ('Политехническая', 60.008926, 30.370952)
    AKADEMICHESKAJA = ('Академическая', 60.012763, 30.395706)
    GRAZHDANSKIY_PROSPECT = ('Гражданский проспект', 60.03481, 30.418087)
    DEVJATKINO = ('Девяткино', 60.049799, 30.442248)
    KUPCHINO = ('Купчино', 59.829887, 30.375399)
    ZVEZDNAYA = ('Звёздная', 59.833228, 30.349616)
    MOSCOVSKAJA = ('Московская', 59.852192, 30.322206)
    PARK_POBEDI = ('Парк Победы', 59.86659, 30.321712)
    ELEKTROSILA = ('Электросила', 59.879425, 30.318658)
    MOSCOVSKIJE_VOROTA = ('Московские Ворота', 59.891924, 30.317751)
    FRUNZENSKAJA = ('Фрунзенская', 59.906155, 30.317509)
    TECHNOLOGICHESKIY_INSTITUT_2 = ('Технологический институт-2', 59.916622, 30.318505)
    SENNAJA_PLOSHAD = ('Сенная площадь', 59.92709, 30.320378)
    NEVSKIJ_PROSPECT = ('Невский проспект', 59.935601, 30.327134)
    GORKOVSKAJA = ('Горьковская', 59.956323, 30.318724)
    PETROGRADSKAJA = ('Петроградская', 59.966465, 30.311432)
    CHERNAJA_RECHKA = ('Чёрная речка', 59.985574, 30.300792)
    PIONERSKAJA = ('Пионерская', 60.002576, 30.296791)
    UDELNAJA = ('Удельная', 60.016707, 30.315421)
    OZERKI = ('Озерки', 60.037141, 30.321529)
    PROSPEKT_PROSVECHENIJA = ('Проспект Просвещения', 60.051416, 30.332632)
    PARNAS = ('Парнас', 60.06715, 30.334128)
    PRIMORSKAJA = ('Приморская', 59.948545, 30.234526)
    VASILEOSTROVSKAJA = ('Василеостровская', 59.942927, 30.278159)
    GOSTINIJ_DVOR = ('Гостиный Двор', 59.934049, 30.333772)
    MAJAKOVSKAJA = ('Маяковская', 59.931612, 30.35491)
    PLOSHAD_ALEKSANDRA_NEVSKOGO_1 = ('Площадь Александра Невского-1', 59.924314, 30.385102)
    ELIZAROVSKAJA = ('Елизаровская', 59.896705, 30.423637)
    LOMONOSOVKAJA = ('Ломоносовская', 59.877433, 30.441951)
    PROLETARSKAJA = ('Пролетарская', 59.865275, 30.47026)
    OBUKHOVO = ('Обухово', 59.848795, 30.457805)
    RIBATSKOE = ('Рыбацкое', 59.830943, 30.500455)
    ULITSA_DYBENKO = ('Улица Дыбенко', 59.907573, 30.483292)
    PROSPEKT_BOLSHEVIKOV = ('Проспект Большевиков', 59.919819, 30.466908)
    LADOZHSKAJA = ('Ладожская', 59.93244, 30.439474)
    NOVOCHERKASSKAJA = ('Новочеркасская', 59.92933, 30.412918)
    PLOSHAD_ALEKSANDRA_NEVSKOGO_2 = ('Площадь Александра Невского-2', 59.92365, 30.383471)
    LIGOVSKIY_PROSPECT = ('Лиговский проспект', 59.920747, 30.355245)
    DOSTOEVSKAJA = ('Достоевская', 59.928072, 30.345746)
    SPASSKAJA = ('Спасская', 59.926839, 30.319752)
    MEZHDUNARODNAJA = ('Международная', 59.869966, 30.379045)
    BUKHARESTSKAJA = ('Бухарестская', 59.883681, 30.369673)
    VOLKOVSKAJA = ('Волковская', 59.896265, 30.35686)
    OBVODNIY_KANAL = ('Обводный канал', 59.914697, 30.349361)
    ZVENIGORODSKAJA = ('Звенигородская', 59.922304, 30.335784)
    SADOVAJA = ('Садовая', 59.927008, 30.317456)
    ADMIRALTEYSKAJA = ('Адмиралтейская', 59.935877, 30.314886)
    SPORTIVNAJA_1 = ('Спортивная-1', 59.952078, 30.291312)
    SPORTIVNAJA_2 = ('Спортивная-2', 59.950365, 30.287356)
    CHKALOVSKAJA = ('Чкаловская', 59.961035, 30.291964)
    KRESTOVSKIJ_OSTROV = ('Крестовский остров', 59.971838, 30.259427)
    STARAJA_DEREVNJA = ('Старая Деревня', 59.989228, 30.255169)
    KOMENDANTSKIY_PROSPECT = ('Комендантский проспект', 60.008356, 30.258915)

    def __init__(self, station_name, lat, lng):
        self.station_name = station_name
        self.lat = lat
        self.lng = lng