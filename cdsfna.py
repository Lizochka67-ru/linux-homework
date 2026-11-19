records = []
with open("cds.fna", "r") as file:
    for line in file:
        line=line.strip()
        if line.startswith(">"):
            records={
                    "metadata": line[1:],
                    "data": ""
                    }
            records.append(record)
        else:
            records[-1]["data"]+=line

