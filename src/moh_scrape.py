from pathlib import Path

from lib import scrape_table

output_path = Path("data/")


def nz_dhb_cases():
    output_filename = "nz_dhb_cases"

    url = "https://www.health.govt.nz/our-work/diseases-and-conditions/covid-19-novel-coronavirus/covid-19-current-situation/covid-19-current-cases"

    fields = {'dhb': str, 'active': int, 'recovered': int, 'deceased': int, 'total': int, 'delta': int}

    start = "Total cases by DHB, "

    scrape_table(output_path, output_filename, url, fields, start, skip_totals=True)


def nz_tests():
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


def nz_dhb_cases_hospital():
    output_filename = "nz_dhb_cases_hospital"

    url = "https://www.health.govt.nz/our-work/diseases-and-conditions/covid-19-novel-coronavirus/covid-19-current-situation/covid-19-current-cases"

    fields = {'dhb': str, 'cases': int}

    start = "Total cases in hospital by DHB</h2>"

    scrape_table(output_path, output_filename, url, fields, start, skip_totals=True)


def nz_tests_by_region():
    output_filename = "nz_tests_by_region"

    url = "https://www.health.govt.nz/our-work/diseases-and-conditions/covid-19-novel-coronavirus/covid-19-current-situation/covid-19-current-cases/covid-19-testing-region"

    fields = {'region': str, 'num_people': int, 'pct_people': str, 'num_tests': int, 'pop': int, 'rate_per_100': float}

    start = "Tests by DHB of residence as at"

    scrape_table(output_path, output_filename, url, fields, start, skip_totals=True)


def run():
    nz_dhb_cases()
    nz_tests()
    nz_dhb_cases_hospital()
    nz_tests_by_region()

if __name__ == "__main__":
    run()
