# https://api.chess.com/pub/titled/GM
usernames_example = {
    "players": [
        "0blivi0usspy",
        "123lt",
        "124chess",
        "1977ivan",
    ]
}
# https://api.chess.com/pub/player/{username}
user_example = {
    "player_id": 26735280,
    "@id": "https://api.chess.com/pub/player/astralpulse",
    "url": "https://www.chess.com/member/astralpulse",
    "name": "Alex Goldin",
    "username": "astralpulse",
    "title": "GM",
    "followers": 114,
    "country": "https://api.chess.com/pub/country/US",
    "location": "Chicago",
    "last_online": 1726936073,
    "joined": 1455562544,
    "status": "premium",
    "is_streamer": False,
    "verified": False,
    "league": "Champion",
    "streaming_platforms": [],
}


def main():
    print("Hello, World!")


if __name__ == "__main__":
    main()
