from stats_grabber import sorted_data

def gen_prometheus_out():
    out = ""
    for lk in sorted_data()["data"]:
        name = lk['name'].replace('-','_')
        name = name.replace(' ','_')
        name = name.replace("ä", "ae")
        name = name.replace("ü", "ue")
        name = name.replace("ö", "oe")
        name = name.replace("Ä", "Ae")
        name = name.replace("Ü", "Ue")
        name = name.replace("Ö", "Oe")


        tmp = f"corona_cases{{lk=\"{name}\"}} {lk['cases']}\n"
        tmp += f"corona_cases_diff{{lk=\"{name}\"}} {lk['cases_diff']}\n"
        tmp += f"corona_case_100k{{lk=\"{name}\"}} {lk['case_100k']}\n"
        tmp += f"corona_case_7d{{lk=\"{name}\"}} {lk['case_7d']}\n"
        tmp += f"corona_case_7d_100k{{lk=\"{name}\"}} {lk['case_7d_100k']}\n"
        tmp += f"corona_deaths{{lk=\"{name}\"}} {lk['deaths']}\n"
        tmp += f"corona_deaths_diff{{lk=\"{name}\"}} {lk['deaths_diff']}\n"
        out += tmp

    return(out)
