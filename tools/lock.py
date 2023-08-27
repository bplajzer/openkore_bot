import pathlib

from jinja2 import Environment, FileSystemLoader

# todo
# ! rework this to use proper OOP
# ! add custom kafra/sell not on the same map as city

lockMaps = {
    "prt_fild07": {
        "city": "prontera",
        "sell": "147 175",
        "kafra": "164 175",
    },
    "prt_fild02": {
        "city": "prontera",
        "sell": "147 175",
        "kafra": "164 175",
    },
    "pay_fild09": {
        "city": "payon",
        "sell": "183 102",
        "kafra": "181 104",
    },
    "pay_fild08": {
        "city": "payon",
        "sell": "183 102",
        "kafra": "181 104",
    },
    "pay_dun02": {
        "city": "payon",
        "sell": "183 102",
        "kafra": "181 104",
    },
    "moc_pryd05": {
        "city": "morocc",
        "sell": "149 102",
        "kafra": "156 97",
    },
    "moc_fild18": {
        "city": "morocc",
        "sell": "149 102",
        "kafra": "156 97",
    },
    "iz_dun03": {
        "city": "izlude",
        "sell": "105 99",
        "kafra": "134 87",
    },
    "in_sphinx3": {
        "city": "morocc",
        "sell": "149 102",
        "kafra": "156 97",
    },
    "in_sphinx2": {
        "city": "morocc",
        "sell": "149 102",
        "kafra": "156 97",
    },
    "gef_fild14": {
        "city": "geffen",
        "sell": "124 70",
        "kafra": "120 62",
    },
    "gef_fild08": {
        "city": "geffen",
        "sell": "124 70",
        "kafra": "120 62",
    },
    "gef_fild07": {
        "city": "geffen",
        "sell": "124 70",
        "kafra": "120 62",
    },
    "iz_dun04": {
        "city": "izlude",
        "sell": "105 99",
        "kafra": "134 87",
    },
    "gl_dun01": {
        "city": "geffen",
        "sell": "124 70",
        "kafra": "120 62",
    },
    "xmas_dun02": {
        "city": "xmas",
        "sell": "141 136",
        "kafra": "150 137",
    },
    "alde_dun04": {
        "city": "aldebaran",
        "sell": "145 122",
        "kafra": "143 119",
    },
    # "abbey01": {
    #     "city": "",
    #     "sell": "",
    #     "kafra": "",
    # },
}

output_path = "./result/lock_map/"
pathlib.Path(f"{output_path}/").mkdir(parents=True, exist_ok=True)
environment = Environment(loader=FileSystemLoader("./templates"))
template = environment.get_template("lockMapMacro.tpl")

for map, data in lockMaps.items():
    lockMap = map
    city = data["city"]
    sell = data["sell"]
    kafra = data["kafra"]
    print(f"Creating macro for: {lockMap}")
    content = template.render(
        lockMap=lockMap,
        city=city,
        sell=sell,
        kafra=kafra,
    )
    with open(f"{output_path}{lockMap}.txt", mode="w+", encoding="utf-8") as message:
        message.write(f"{content}\n")
        print(f"✓ {lockMap} saved!")
