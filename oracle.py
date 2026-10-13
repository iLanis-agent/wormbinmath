import json, math

def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def plural(n, word, form=None): return str(jsnum(n)) + " " + (word if n == 1 else (form or word + "s"))
def fmt(x): return str(jsnum(x))
def round0(x): return jsnum(math.floor(x + 0.5))
def round1(x): return jsnum(math.floor(x * 10 + 0.5) / 10)

SCRAP_KG = 0.5
FEED_RATE = 3.5
WORM_G_M2 = 500
CASTINGS_L = 5

def bin_plan(people):
    if not (people > 0):
        return {"error": "the people must be positive"}
    scraps = round1(people * SCRAP_KG)
    area = round1(people * SCRAP_KG / FEED_RATE)
    if area <= 0.2: verdict = "a shoebox bin"
    elif area <= 0.6: verdict = "a tote bin"
    else: verdict = "a stacked tower"
    return {"scraps": scraps, "area": area, "verdict": verdict}

def worm_plan(areaM2):
    if not (areaM2 > 0):
        return {"error": "the area must be positive"}
    grams = round0(areaM2 * WORM_G_M2)
    if grams <= 250: verdict = "a starter handful"
    elif grams <= 500: verdict = "a half-kilo start"
    else: verdict = "a kilo club"
    return {"grams": grams, "verdict": verdict}

def harvest_plan(areaM2):
    if not (areaM2 > 0):
        return {"error": "the area must be positive"}
    liters = round1(areaM2 * CASTINGS_L)
    if liters <= 2: verdict = "a houseplant scoop"
    elif liters <= 5: verdict = "a balcony boost"
    else: verdict = "a garden supply"
    return {"liters": liters, "verdict": verdict}

def render_bin(r, people):
    return ("Your " + fmt(people) + "-person kitchen at a labeled " + fmt(SCRAP_KG) + " kg of scraps each a week makes "
            + fmt(r["scraps"]) + " kg - a labeled " + fmt(FEED_RATE) + " kg per m2 feed rate names a " + fmt(r["area"]) + " m2 bin, " + r["verdict"] + ".")

def render_worm(r, areaM2):
    return ("Your " + fmt(areaM2) + " m2 bin at a labeled " + fmt(WORM_G_M2) + " g of worms per m2 starts with "
            + fmt(r["grams"]) + " g of worms - " + r["verdict"] + ".")

def render_harvest(r, areaM2):
    return ("Your " + fmt(areaM2) + " m2 bin at a labeled " + fmt(CASTINGS_L) + " L per m2 a month gives "
            + fmt(r["liters"]) + " L of castings a month - " + r["verdict"] + ".")

cases = []
def add(fn, f, rf, args):
    r = f(*args)
    c = {"fn": fn, "args": args, "result": r}
    if "error" not in r: c["render"] = rf(r, *args)
    cases.append(c)

for a in [[4],[2],[1],[6],[3],[8],[5],[10],[0],[12]]:
    add("binPlan", bin_plan, render_bin, a)
for a in [[0.6],[0.1],[0.2],[1],[2],[0.4],[1.5],[0.5],[0],[3]]:
    add("wormPlan", worm_plan, render_worm, a)
for a in [[0.6],[0.1],[1],[2],[0.4],[1.5],[0.2],[3],[0],[0.8]]:
    add("harvestPlan", harvest_plan, render_harvest, a)
json.dump(cases, open("expected.json", "w"), separators=(",", ":"))
print(len(cases), "cases")
