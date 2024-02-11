from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.translation import get_language, gettext, activate

def home(request):
    # Activate the desired language
    language = request.LANGUAGE_CODE
    cur_language = get_language()
    try:
        activate(language)

        # Translated text strings
        city_name_text = _("Enter a City Name")
        current_weather_heading = _("Current Weather")
        temperature_text = _("Temperature:")
        wind_text = _("Wind:")
        humidity_text = _("Humidity:")
        forecast_heading = _("5-Day Forecast")
        search_btn_text = _("Search")
        location_btn_text = _("Use Current Location")
        days_forecast = [_("Day 1"), _("Day 2"), _("Day 3"), _("Day 4"), _("Day 5")]

        return render(request, "index.html", {'city_name_text': city_name_text,
                                              'current_weather_heading': current_weather_heading,
                                              'temperature_text': temperature_text,
                                              'wind_text': wind_text,
                                              'humidity_text': humidity_text,
                                              'forecast_heading': forecast_heading,
                                              'search_btn_text': search_btn_text,
                                              'location_btn_text': location_btn_text,
                                              'days_forecast': days_forecast})
    finally:
        activate(cur_language)
