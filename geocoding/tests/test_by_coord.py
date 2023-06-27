import sys

import pytest

from geocoding.geocode.by_coord import Get_by_coord

class Test_Get_by_coord:


    @pytest.mark.parametrize('lat,lon,focus_name',[     (55.66881,37.56035,"улица Гарибальди"),
                                                        (56.98217,40.98427,"Мопровская улица"),
                                                        (57.95894,56.2389,"Кузбасская улица"),
                                                        (51.81971,12.23873,'Lutherstraße')
    ])
    def test_get_street_name(self,lat,lon,focus_name):
        get_name_by_coord = Get_by_coord()
        result = ''.join(get_name_by_coord.get_address(lat=lat,lon=lon).split(',')).strip()
        assert focus_name in result

    @pytest.mark.parametrize('lat,lon,res_name', [(61.66321, 50.83429, "92 Первомайская улица"),
                                                    (54.98423, 73.37294, "2 улица Карла Либкнехта"),
                                                    (54.73351, 55.94913, "64 улица Достоевского"),
                                                    (38.56059, 68.75594, '134 проспект Абуали Сино')
                                                    ])
    def test_get_address_name(self,lat,lon,res_name):
        get_name_by_coord = Get_by_coord()
        result = ''.join(get_name_by_coord.get_address(lat=lat, lon=lon).split(',')[:2]).strip()
        assert result == res_name

    def test_match_str_int_coord(self):
        get_name_by_coord = Get_by_coord()
        assert get_name_by_coord.get_address(lat=58.02262, lon=38.85201) == get_name_by_coord.get_address(lat='58.02262', lon='38.85201')