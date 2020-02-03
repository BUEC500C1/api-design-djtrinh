import weather_api


def test_num_input():
    api = weather_api.weather_api();
    assert api.get_weather("1353") == -1


def test_wrong_iata_input():
    api = weather_api.weather_api();
    assert api.get_weather("wjwkw") == -1


def test_nonexistant_iata():
    api = weather_api.weather_api();
    assert api.get_weather("itv") == -1


def test_symbol_input():
    api = weather_api.weather_api();
    assert api.get_weather("^sj") == -1
