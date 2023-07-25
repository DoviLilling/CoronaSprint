def get_sprint_parameters():
    daw = int(input("What's the number of days and workers? "))
    s = int(input("How many slots per day? "))
    w = set(range(daw))
    return w, s


def setup(p_workers):
    workers_ex = {}
    for w in p_workers:
        workers_ex[w] = set([w])
    return workers_ex


def fill_slots_recursive(p_day, p_slots, p_workers, p_workers_exceptions, p_indent):
    if len(p_day) == p_slots:
        return True
    for candidate in [w for w in p_workers if len(p_workers_exceptions[w]) < len(p_workers) and w not in p_day]:
        # print(f'{p_indent}candidate: {candidate}')
        exception_found = any(list(map(lambda worker_in_day: worker_in_day in p_workers_exceptions[candidate], p_day)))
        if not exception_found:
            p_day.add(candidate)
            # print(f'{p_indent}p_day: {p_day}')
            if fill_slots_recursive(p_day, p_slots, p_workers, p_workers_exceptions, p_indent + '   '):
                return True
            else:
                p_day.remove(candidate)
    return False


def setup_day(p_workers, p_slots, p_workers_exceptions):
    day = set()
    # print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    fill_slots_recursive(day, p_slots, p_workers, p_workers_exceptions, '')
    # print(f'day: {day}')
    for worker in day:
        p_workers_exceptions[worker].update(day)
    # print(f'p_workers_exceptions: {p_workers_exceptions}')
    return day


if __name__ == '__main__':
    workers, slots = get_sprint_parameters()
    print(f'workers: {workers}, slots: {slots}')
    days = len(workers)
    print(f'days: {days}')
    workers_exceptions = setup(workers)
    # setup_day(workers, workers_per_day, workers_exceptions)
    for i in range(days):
        print(f'day {i}: ', setup_day(workers, slots, workers_exceptions))
