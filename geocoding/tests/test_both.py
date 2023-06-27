from geocoding.geocode.by_addresses import Get_by_addresses
from geocoding.geocode.by_coord import Get_by_coord
import pytest

@pytest.mark.parametrize('street,city,lat,lon',[    ('9 улица Расплётина','Рыбинск',58.03873,38.8621),
                                                    ('1 улица Миронова', "Новокуйбышевск", 53.09789,49.95127),
                                                    ('56 улица Щорса',"Красноярск",55.99157,'92.94834'),
                                                    ('14 улица Патриотов','Кемерово',55.31915,86.07954)


])

def test_both_coord(street,city,lat,lon):
    obj_by_adr = Get_by_addresses()
    obj_by_coord = Get_by_coord()
    assert obj_by_adr.get_coord(street=street,city=city) == obj_by_coord.get_excat_coord(lat=lat,lon=lon)