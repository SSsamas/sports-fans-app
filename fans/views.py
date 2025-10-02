from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from json import JSONDecodeError

teams_data = [
    {"name": "Real Madrid", "sport": "Football", "description": "Spanish football club"},
    {"name": "Los Angeles Lakers", "sport": "Basketball", "description": "NBA team"},
    {"name": "New York Yankees", "sport": "Baseball", "description": "MLB team"},
    {"name": "Manchester United", "sport": "Football", "description": "English football club"},
]


def get_translations(lang: str) -> dict:
    """Return UI strings for the given language code (en, ru)."""
    en = {
        "brand": "Sports Fans",
        "hero_title": "Your Hub for Sports Passion",
        "hero_subtitle": "Choose your favorite teams, switch themes, and make the app yours. All preferences are saved in your browser.",
        "popular_teams": "Popular Teams",
        "customize": "Customize Your Experience",
        "favorite_teams": "Favorite Teams",
        "theme": "Theme",
        "language": "Language",
        "save": "Save Settings",
        "current_prefs": "Current Preferences",
        "favorites": "Favorites",
        "no_teams": "No teams selected",
        "last_page": "Last visited page",
        "footer": "Built for sports fans",
    }
    ru = {
        "brand": "Спортивные фанаты",
        "hero_title": "Твой центр спортивной страсти",
        "hero_subtitle": "Выбирай любимые команды, меняй темы и настраивай приложение под себя. Все предпочтения сохраняются в браузере.",
        "popular_teams": "Популярные команды",
        "customize": "Настройка интерфейса",
        "favorite_teams": "Любимые команды",
        "theme": "Тема",
        "language": "Язык",
        "save": "Сохранить",
        "current_prefs": "Текущие настройки",
        "favorites": "Избранное",
        "no_teams": "Команды не выбраны",
        "last_page": "Последняя посещённая страница",
        "footer": "Создано для спортивных фанатов",
    }
    return ru if str(lang).lower() == "ru" else en


def home(request):
    # Read cookies with safe defaults
    try:
        favorite_teams = json.loads(request.COOKIES.get("favorite_teams", "[]"))
        if not isinstance(favorite_teams, list):
            favorite_teams = []
    except JSONDecodeError:
        favorite_teams = []

    theme = request.COOKIES.get("theme", "light")
    language = request.COOKIES.get("language", "en")
    last_page = request.COOKIES.get("last_page", "/")

    t = get_translations(language)

    context = {
        "teams": teams_data,
        "favorite_teams": favorite_teams,
        "theme": theme,
        "language": language,
        "last_page": last_page,
        "t": t,
    }
    response = render(request, "fans/home.html", context)
    # Track last visited page
    response.set_cookie("last_page", request.path, samesite="Lax")
    return response


def set_settings(request):
    if request.method == "POST":
        favorite_teams = request.POST.getlist("teams")
        theme = request.POST.get("theme", "light")
        language = request.POST.get("language", "en")

        response = redirect("home")
        # Persist cookies for 30 days, Lax is fine for this app
        cookie_opts = {"max_age": 60 * 60 * 24 * 30, "samesite": "Lax"}
        response.set_cookie("favorite_teams", json.dumps(favorite_teams), **cookie_opts)
        response.set_cookie("theme", theme, **cookie_opts)
        response.set_cookie("language", language, **cookie_opts)
        return response
    return redirect("home")
