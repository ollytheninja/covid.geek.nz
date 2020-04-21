from pathlib import Path

from src.lib import scrape_table


def nz_dhb_cases():
    output_path = Path("../data/")
    output_filename = "nz_dhb_cases"

    url = "https://www.health.govt.nz/our-work/diseases-and-conditions/covid-19-novel-coronavirus/covid-19-current-situation/covid-19-current-cases"

    fields = {'dhb': str, 'active': int, 'recovered': int, 'deceased': int, 'total': int, 'delta': int}

    start = "Total cases by DHB, "

    scrape_table(output_path, output_filename, url, fields, start, skip_totals=True)


def nz_tests():
    output_path = Path("../data/")
    output_filename = "nz_tests"
    output_path.mkdir(parents=True, exist_ok=True)

    url = "https://www.health.govt.nz/our-work/diseases-and-conditions/covid-19-novel-coronavirus/covid-19-current-situation/covid-19-current-cases"
    start = "COVID-19 - tests by day and cumulative"
    fields = {
        "date": str,
        "count": int,
        "total": int,
    }
    scrape_table(output_path, output_filename, url, fields, start)


def run():
    nz_dhb_cases()
    nz_tests()


if __name__ == "__main__":
    run()
