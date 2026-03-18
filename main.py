import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players = json.load(players_file)
        for player in players:
            race, _ = Race.objects.get_or_create(
                        name=player["race"]["name"],
                        defaults={
                            "description": player["race"]["description"]
                        }
            )

            for skill in player["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    defaults={
                        "bonus": skill["bonus"],
                        "races": race
                    }
                )

            guild = Guild.objects.get_or_create(
                name=player["guild"]["name"],
                defaults={
                    "description": player["guild"]["description"]
                }
            )
            Player.objects.get_or_create(
                name=player["name"],
                defaults={
                    "email": player["email"],
                    "bio": player["bio"],
                    "race": race,
                    "guild": guild
                }
            )


if __name__ == "__main__":
    main()
