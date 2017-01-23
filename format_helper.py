import glob
import json

#format
for fn in glob.iglob("schemas/*/*.json"):
    with open(fn,encoding="utf8") as f:
        obj=json.load(f)
    with open(fn,"w",encoding="utf8") as f:
        json.dump(obj,f, indent=1, sort_keys=True)

#format
for fn in glob.iglob("docs/**/*.rst"):
    with open(fn,encoding="utf8") as f:
        lines=[l.rstrip().replace("\t","    ") for l in f]
    with open(fn,"w",encoding="utf8",newline="") as f:
        for l in lines:
            f.write(l)
            f.write("\n")
        if lines[-1]:
            f.write("\n")
        
