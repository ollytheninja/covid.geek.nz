import json
import re
from datetime import datetime

import pytz
import requests


def scrape_table(output_path, output_filename, url, fields, start, skip_totals=False):
    output_path.mkdir(parents=True, exist_ok=True)

    response = requests.get(url)
    data = response.text

    start = data.find(start)
    end = data.find("</table>", start)
    table = data[start:end]

    regex = r"\n\t+".join([r'<td( nowrap="nowrap")?>(?P<' + field + r">.*?)</td>" for field in fields])

    rows = re.finditer(regex, table, re.DOTALL)

    now = datetime.now(tz=pytz.utc)
    nzst = pytz.country_timezones.get("nzst")

    output = {
        "_meta": {
            "retrieved_utc": now.isoformat(),
            "retrieved_nzst": now.astimezone(nzst).isoformat(),
            "url": url,
        },
        "data": []
    }

    for row in rows:
        out = {}
        for field, t in fields.items():
            try:
                value = t(row.group(field))
            except:
                value = ""
            out[field] = value

        output['data'].append(out)

    if skip_totals:
        output['data'] = output['data'][:-1]

    with open(output_path / (output_filename + ".json"), "w") as f:
        json.dump(output, f, indent=4)
