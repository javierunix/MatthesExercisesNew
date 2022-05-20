def city_contry(city, country, population=None):
    """Function to format neatly the city and country."""
    if population:
        formatted_city = f"{city}, {country} - population: {population}"
    else:
        formatted_city = f"{city}, {country}"
    return formatted_city.title()
