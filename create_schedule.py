from pathlib import Path
from typing import Union

import pandas as pd
from ics import Calendar, Event


def create_schedule(filename: Union[Path, str], output_filename: str = "running_schedule.ics") -> None:
    df = pd.read_csv(filename, parse_dates=["Date"], index_col=0)
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

    with open(output_filename, "w") as f:
        f.writelines(c.serialize_iter())

if __name__ == "__main__":
    create_schedule(filename="marathon_schedule.csv", output_filename="marathon_schedule.ics")
