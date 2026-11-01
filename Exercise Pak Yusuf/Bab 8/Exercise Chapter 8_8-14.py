def make_car(manufacturer, model, **car_info):
    """Buat dictionary berisi informasi tentang sebuah mobil."""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info


car = make_car('subaru', 'outback', color='biru', tow_package=True)
print(car)