
import pendulum

# Return the list [] of all days during one entire year.
def  get_days_range_yearly_from_now():
    start = pendulum.now()
    end = start.add(years=1)
    period = pendulum.period(start, end)

    days_list = []

    for day in period.range('days'):
        days_list.append(day)

    return days_list


# Return a list [] of group of a given number of days during one entire year.
def get_days_groups_yearly_from_now(num_days: int):
    start_date = pendulum.now()
    end_date = start_date.add(years=1)
    num_chunks = (end_date - start_date).days - num_days + 2
    result = []
    for i in range(num_chunks):
        chunk = [start_date.add(days=x) for x in range(i, i + num_days)]
        result.append([date for date in chunk])
        # result.append([date.format("DD/MM/YYYY") for date in chunk])
    return result



