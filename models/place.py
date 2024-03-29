#!/usr/bin/python3
"""Place class module, this class will inherit from base model
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represents place for app or console

        Attributes:
            city_id (str): City.id
            user_id (str): User.id
            name (str): name of place
            description (str): description of place
            number_rooms (integer): number of rooms in place
            number_bathrooms (integer): number of bath rooms in place
            max_guest (integer): max capacity og guests
            price_by_night (integer): price by night
            latitude (float): latitude of place
            longitude (float): longtude of place
            amenity_ids (list): the list of Amenity.id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
