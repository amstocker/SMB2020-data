import data


if __name__ == "__main__":
    
    # First run `python data.py` to build data set.
    tournaments = data.load_tournaments()
    id_to_name = data.load_id_to_name_map()