import pytest
from geocoding.geocode.by_addresses import Get_by_addresses
class Test_Get_by_addresses:

    ''' При проверке координат, приводим вещественное число к 3 знакам после запятой'''

    @pytest.mark.parametrize('street,city, res ', [
                                                ("Сысольское шоссе", 'Сыктывкар',[61.636,50.812]),
                                                ( "Paddock street", "Watertown",[43.969, -75.916]),
                                                ("二环南路西段辅路", "Сиань", [34.231, 108.931]),
                                                ("Rostocker Straße","Egelsbach", [49.966,8.668]),
                                                ('18к1 Маршала Захарова',"Санкт-Петербург",[59.858, 30.171]),
                                                ('4 Pekanpatama', "Jyväskylä", [62.222, 25.786]),
                                                ('3 Дорожная улица','Москва',[55.615,37.629]),
    ])

    def test_get_coord(self,street,city,res):
        get_coord_obj = Get_by_addresses()
        result = [i for i in get_coord_obj.get_coord(street=street,city=city)]
        result[0],result[1] = round(float(result[0]),3) ,round(float(result[1]),3)
        assert result == [res[0],res[1]]

    @pytest.mark.parametrize('country,res',[        ('Россия', 60189),
                                                    ('Russia',60189 ),
                                                    ("Китай", 270056),
                                                    ("Иран",304938),
                                                                                ] )
    def test_get_osm_id_by_contry(self,country,res):
        get_osm_id = Get_by_addresses()
        result = get_osm_id.get_osm_id_by_country(country)
        assert result == res

    @pytest.mark.parametrize('street,city,res', [        ("улица Рубинштейна","Санкт-Петербург",1),
                                                         ("Московское шоссе","Самара",4),
                                                         ("Улица Гагарина", "Билярск",2),
                                                        ("Große Reichenstraße", "Гамбург",2)
    ])
    def test_get_volume_in_city(self,street,city,res):
        get_osm_num = Get_by_addresses()
        result = get_osm_num.get_objects_volume_in_city(street=street,city=city)
        assert result == res

