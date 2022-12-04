import pandas as pd
from ics import Calendar, Event

if __name__ == "__main__":
    df = pd.read_csv("half_marathon_schedule.csv", parse_dates=["Date"], index_col=0)
    s = df.squeeze("columns")

    c = Calendar()

    for date, miles in s.items():
        if miles == 0:
            pass
        else:
            e = Event(name=f"Run {miles} miles", begin=date)
            e.make_all_day()
            c.events.add(e)
    print(c.events)

with open("halfmarathon.ics", "w") as f:
    f.writelines(c.serialize_iter())
