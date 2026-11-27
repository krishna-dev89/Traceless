
import requests

PLATFORMS = {
    "GitHub": "https://github.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "Instagram": "https://www.instagram.com/{}/",
    "Pinterest": "https://www.pinterest.com/{}/",
    "Medium": "https://medium.com/@{}",
}


def check_profile(platform, username):
    url = PLATFORMS[platform].format(username)

    try:
        response = requests.get(
            url,
            headers={"User-Agent": "TraceLess/1.0"},
            timeout=10
        )

        if response.status_code == 200:
            status = "Potential match"
        elif response.status_code == 404:
            status = "Not found"
        else:
            status = "Unable to verify"

        return {
            "platform": platform,
            "url": url,
            "status": status
        }

    except requests.RequestException:
        return {
            "platform": platform,
            "url": url,
            "status": "Connection error"
        }


def search_username(username):
    results = []

    for platform in PLATFORMS:
        results.append(check_profile(platform, username))

    return results
