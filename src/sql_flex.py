import re
import pandas as pd

def flex(sql_query):
    results = {}
    for value in re.findall(r"(([A-Za-z.]+ in )*(((\[.*\]|\w*) like )*\(*'%*.+%*'\)*( as (\w|\[.*\])*)*))", sql_query.lower()):
        splited_values = value[0].split(" ")
        val = "".join(splited_values[2:])
        if "as" in value[0] and splited_values[2] != "key":
            results[re.sub("\'|\"", "", splited_values[0])] = re.sub(r"\W", "", val)
        elif "like" in value[0] or "in" in value[0]:
            val = val[:-1] if val[-1] == ")" and val[0] != "(" else val
            results[re.sub("\'|\"", "", val)] = re.sub(r"\[|\]", "", splited_values[0])
    df = pd.DataFrame(results.items(), columns=["Harcoded_value", "Column_Name"])
    return df