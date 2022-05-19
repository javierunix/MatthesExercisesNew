def make_car(manufacturer, model, **car_info):
    """
    Return a dictionary with the car information.
    Always recive manufacturer and model as argument,
    and an arbitrary number of keywords arguments.
    """
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info


car = make_car('subaru', 'imprezza', color='silver', year=2012,
               tow_package=True)
print(car)
