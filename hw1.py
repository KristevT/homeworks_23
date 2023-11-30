"""Top 3 salaries module."""


def top3_salaries_stats(
    departments: dict[str, float | int],
    excluding: tuple[str, ...] = None,
    )-> tuple[
        tuple[str, float | int],
        tuple[str, float | int],
    ]:
    """Find 3 most- and least-paid departments in a given dictionary by average value.

    Args:
        departments: a dictionary with departments names their values.
        excluding: tuple with names of departments to be excluded from stats, defaults to None.

    Returns:
        stats: tuple of top 3 most and least paid departments with their average salaries.
    """
    avg_salaries = {}
    for department, workers in departments.items():
        if excluding is None or department not in excluding:
            salaries = workers.values()
            avg_salary = round(sum(salaries) / len(salaries), 2) if salaries else 0
            avg_salaries[department] = avg_salary

    salaries_sorted = sorted(avg_salaries.items(), key=lambda srt: srt[1], reverse=True)
    top3_most_paid = salaries_sorted[:3]
    top3_least_paid = salaries_sorted[-3:][::-1]
    return tuple(top3_most_paid), tuple(top3_least_paid)
