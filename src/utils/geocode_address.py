
import geopy
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError

def geocode_address(address: str, timeout: int = 10):
    """
    Geocode a textual address using Nominatim.
    
    Parameters
    ----------
    address : str
        Human-readable address
    timeout : int
        Timeout in seconds for the request

    Returns
    -------
    dict | None
        Dictionary with address, latitude, longitude, or None if not found
    """
    geolocator = Nominatim(user_agent="paris_daycares")

    try:
        location = geolocator.geocode(address, timeout=timeout)

        if location:
            return {
                "address": location.address,
                "latitude": location.latitude,
                "longitude": location.longitude,
            }
        else:
            return None

    except (GeocoderTimedOut, GeocoderServiceError) as e:
        print(f"Geocoding error for '{address}': {e}")
        return None
