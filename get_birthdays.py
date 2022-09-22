from datetime import datetime, timedelta

users = [{"name": "Artem", "birthday": datetime(1995, 9, 23)},
         {"name": "Olia", "birthday": datetime(1998, 12, 24)},
         {"name": "Vicor", "birthday": datetime(1997, 7, 14)},
         {"name": "Maria", "birthday": datetime(1998, 9, 17)},
         {"name": "Mikola", "birthday": datetime(1994, 11, 25)},
         {"name": "Tomas", "birthday": datetime(1990, 9, 23)},
         {"name": "Justin", "birthday": datetime(2000, 9, 5)},
         {"name": "Maya", "birthday": datetime(2003, 12, 9)},
         {"name": "Dima", "birthday": datetime(1988, 9, 27)},
         {"name": "Liza", "birthday": datetime(1978, 9, 25)},
         {"name": "Vlad", "birthday": datetime(1999, 1, 29)},
         {"name": "Kiril", "birthday": datetime(2004, 3, 27)}]

week_days = {"Monday": [], "Tuesday": [],
             "Wednesday": [], "Thursday": [], "Friday": []}

pattern = "%Y.%m.%d"


def get_birthdays_per_week(users):

    for user in users:

        name, birthday = user["name"], user["birthday"].strftime("%m.%d")

        for date in [(datetime.today() + timedelta(days=i)).strftime(pattern)
                     for i in range(1, 8)]:

            if birthday in date:

                date = datetime.strptime(date, pattern)

                if date.isoweekday() <= 5:
                    week_days[date.strftime("%A")].append(name)
                else:
                    week_days["Monday"].append(name)

    for key, value in week_days.items():
        if value:
            print(f"{key}: {', '.join(value)}")


if __name__ == "__main__":
    get_birthdays_per_week(users)
