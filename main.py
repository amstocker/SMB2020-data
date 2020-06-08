import data


if __name__ == "__main__":
    # Already did these...
    # data.dump_tournaments()
    # data.dump_tournament_participants()

    tournaments = data.load_tournaments()

    for t in tournaments:
        print(t["index"], [p["participant"]["display_name"] for p in t["participants"]])
