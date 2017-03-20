import glob
import json
import collections

# format
for fn in glob.iglob("schemas/*/*.json"):
    with open(fn, encoding="utf8") as f:
        so = f.read()
    obj = json.loads(so, object_pairs_hook=collections.OrderedDict)
    sn = json.dumps(obj, indent=1)
    if sn != so:
        with open(fn, "w", encoding="utf8") as f:
            f.write(sn)


# format
for fn in glob.iglob("docs/**/*.rst"):
    with open(fn, encoding="utf8", newline="") as f:
        so = f.read()
    lines = [l.rstrip().replace("\t", "    ") for l in so.splitlines()]
    if lines[-1]:
        lines.append("")
    lines.append("")
    sn = "\n".join(lines)
    if sn != so:
        with open(fn, "w", encoding="utf8", newline="") as f:
            f.write(sn)
