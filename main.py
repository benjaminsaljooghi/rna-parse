from pathlib import Path
from collections import defaultdict
from stringbuilder import StringBuilder

directory = Path("/media/dperrin/ssd_data/riboProf/temp2020/") 
temp1 = Path(directory, "temp1.txt")


# HWI-1KL121:133:C0F6PACXX:2:1101:1918:1952       0       AK156638.4.1396 1359    1       27M     *       0       0       GACCGGGGTCCGGTGCGGAGAGCCGTT     4=DFFFFHFHHHJIIJJJJJJJJJJJJ        AS:i:0  XS:i:0  XN:i:0  XM:i:0  XO:i:0  XG:i:0  NM:i:0  MD:Z:27 YT:Z:UU
# HWI-1KL121:133:C0F6PACXX:2:1101:4829:1805       0       BK000964.8123.12852     1193    1       25M     *       0       0       CGTGGCGCAATGAAGGTGAAGGGCC       4=BDFFFHHHHHJJJJHIJJJJJJJ  AS:i:0  XS:i:0  XN:i:0  XM:i:0  XO:i:0  XG:i:0  NM:i:0  MD:Z:25 YT:Z:UU
# HWI-1KL121:133:C0F6PACXX:2:1101:2361:1874       4       *       0       0       *       *       0       0       GACACTCATGAGTCCACTGGGCATCACC    1BDFFFFHHHHHIJJJJJJJJJIJJJJJ       YT:Z:UU

f = open(str(temp1), "r")

frequency_table = {
    # "full_id": defaultdict(int),
    "id_a": defaultdict(int),
    "rna": defaultdict(int),
}


def parse(line):
    split = line.split("\t")
    
    _id = split[0]
    _id_split = _id.split(":")
    
    id_a = _id_split[0]
    num_a = _id_split[1]
    id_b = _id_split[2]
    num_b = _id_split[3]
    num_c = _id_split[4]
    num_d = _id_split[5]
    num_e = _id_split[6]

    rna = split[9]

    return {
        # "full_id": _id,
        "id_a": id_a,
        "rna": rna,
    }


i = 0
for line in f:
    if line.startswith("@"):
        continue
    # i += 1
    # if i > 100:
        # break

    parsed = parse(line)
    for key, val in parsed.items():
        frequency_table[key][val] += 1


f.close()



report = StringBuilder()


for _type, frequencies in frequency_table.items():

    report.writeline(_type)
    for value, frequency in frequencies.items():
        report.writeline(f"{value}, {frequency}")

    report.writeline()


report.writeto(Path("output.txt"))