from pathlib import Path
from collections import defaultdict
from stringbuilder import StringBuilder

directory = Path("/media/dperrin/ssd_data/riboProf/temp2020/") 

temps = [Path(directory, f"temp{i}.txt") for i in range(1, 16)]


# temp1 = Path(directory, "temp1.txt")

# HWI-1KL121:133:C0F6PACXX:2:1101:1918:1952       0       AK156638.4.1396 1359    1       27M     *       0       0       GACCGGGGTCCGGTGCGGAGAGCCGTT     4=DFFFFHFHHHJIIJJJJJJJJJJJJ        AS:i:0  XS:i:0  XN:i:0  XM:i:0  XO:i:0  XG:i:0  NM:i:0  MD:Z:27 YT:Z:UU
# HWI-1KL121:133:C0F6PACXX:2:1101:4829:1805       0       BK000964.8123.12852     1193    1       25M     *       0       0       CGTGGCGCAATGAAGGTGAAGGGCC       4=BDFFFHHHHHJJJJHIJJJJJJJ  AS:i:0  XS:i:0  XN:i:0  XM:i:0  XO:i:0  XG:i:0  NM:i:0  MD:Z:25 YT:Z:UU
# HWI-1KL121:133:C0F6PACXX:2:1101:2361:1874       4       *       0       0       *       *       0       0       GACACTCATGAGTCCACTGGGCATCACC    1BDFFFFHHHHHIJJJJJJJJJIJJJJJ       YT:Z:UU

def get_rna(line):
    return line.split("\t")[9]

table = defaultdict(int)

for temp in temps:
    f = open(str(temp), "r")
    for line in f:
        if line.startswith("@"):
            continue
        rna = get_rna(line)
        table[rna] += 1
    f.close()

table_sorted = {k: v for k, v in sorted(table.items(), key = lambda item: item[1], reverse=True)}

report = StringBuilder()
for value, frequency in table_sorted.items():
    if frequency > 1:
        report.writevals(value, frequency)
report.writeline()
report.writeto(Path("output.tsv"))