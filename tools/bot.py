import pathlib

import inquirer
from jinja2 import Environment, FileSystemLoader

# todo
# ! rework this to use proper OOP
# ! create from variable
# ! presets

preset = [
    inquirer.List(
        "use",
        message="Use preset?",
        choices=["no", "yes"],
    ),
]
preset_a = inquirer.prompt(preset)

if preset_a["use"] == "no":
    questions = [
        inquirer.Text("account", message="Login"),
        inquirer.Text(
            "follow", message="Name of character to follow [Blank for party leader]"
        ),
        inquirer.List(
            "connection_type",
            message="How bot should connect to server",
            choices=["cli", "proxy"],
        ),
        inquirer.List(
            "loot_action",
            message="What to do with loot",
            choices=["both", "store", "sell"],
        ),
        inquirer.List(
            "party_setup",
            message="How to setup party",
            choices=["share_exp", "share_both", "share_items"],
        ),
        inquirer.List(
            "max_weight",
            message="Max weight before sell/storage",
            choices=["50%", "70%", "90%"],
        ),
        inquirer.List(
            "bot_type",
            message="Party leader or party member",
            choices=["member", "leader"],
        ),
        inquirer.List(
            "autoloot",
            message="Autoloot on login",
            choices=["yes", "no"],
        ),
        inquirer.List(
            "attack_behaviour",
            message="How bot should interact with monsters",
            choices=["aggresive", "supportive", "passive"],
        ),
        inquirer.List(
            "follow_distance",
            message="How far from party leader bot should stay",
            choices=["short", "regular", "long"],
        ),
        inquirer.List(
            "arrows",
            message="Do this bot use arrows?",
            choices=["no", "yes"],
        ),
        inquirer.List(
            "customSetMapLock",
            message="Set mapLock by macro",
            choices=["yes", "no"],
        ),
        inquirer.List(
            "attackDistanceAuto",
            message="If auto detect attack distance attackDistanceAuto",
            choices=["yes", "no"],
        ),
        inquirer.List(
            "party_macro",
            message="Shared party macro",
            choices=["no", "1", "2", "3"],
        ),
        inquirer.List(
            "aspd_potion",
            message="Use aspd potion",
            choices=["no", "Concentration", "Awakening", "Berserk"],
        ),
        inquirer.List(
            "default_heal_items",
            message="Add multi heal",
            choices=["no", "yes"],
        ),
        inquirer.List(
            "customSetMaxPotion",
            message="Carry 20 or 200 healing potions [0 = 20; 1=200]",
            choices=["0", "1"],
        ),
        inquirer.List(
            "route_step",
            message="How many steps bot will try to move at once",
            choices=["15", "8", "5"],
        ),
        inquirer.List(
            "st_job",
            message="First job class",
            choices=[
                "novice",
                "swordman",
                "mage",
                "archer",
                "merchant",
                "thief",
                "acolyte",
                "tekwondo",
            ],
        ),
        inquirer.List(
            "nd_job",
            message="Second job class",
            choices=[
                "knight",
                "crusader",
                "wizard",
                "sage",
                "hunter",
                "bard",
                "dancer",
                "blacksmith",
                "alchemist",
                "assassin",
                "rogue",
                "priest",
                "monk",
                "soul_link",
            ],
        ),
    ]
    answers = inquirer.prompt(questions)


    if answers["connection_type"] == "cli":
        connection_type = "XKore 0"
    elif answers["connection_type"] == "proxy":
        connection_type = (
            "XKore 3\n"
            "XKore_listenPort 6901"
        )


    if answers["loot_action"] == "both":
        loot_action = (
            "sellAuto 1\n"
            "storageAuto 1"
        )
    elif answers["loot_action"] == "store":
        loot_action = (
            "sellAuto 0\n"
            "storageAuto 1"
        )
    elif answers["loot_action"] == "sell":
        loot_action = (
            "sellAuto 1\n"
            "storageAuto 0"
        )


    if answers["party_setup"] == "share_both":
        party_setup = (
            "partyAuto 1\n"
            "partyAutoShare 1\n"
            "partyAutoShareItem 1\n"
            "partyAutoShareItemDiv 1"
        )
    elif answers["party_setup"] == "share_exp":
        party_setup = (
            "partyAuto 1\n"
            "partyAutoShare 1\n"
            "partyAutoShareItem 0\n"
            "partyAutoShareItemDiv 0"
        )
    elif answers["party_setup"] == "share_items":
        party_setup = (
            "partyAuto 1\n"
            "partyAutoShare 0\n"
            "partyAutoShareItem 1\n"
            "partyAutoShareItemDiv 1"
        )


    if answers["max_weight"] == "50%":
        max_weight = (
            "itemsMaxWeight 50\n"
            "itemsMaxWeight_sellOrStore 50"
        )
    elif answers["max_weight"] == "70%":
        max_weight = (
            "itemsMaxWeight 70\n"
            "itemsMaxWeight_sellOrStore 70"
        )
    elif answers["max_weight"] == "90%":
        max_weight = (
            "itemsMaxWeight 90\n"
            "itemsMaxWeight_sellOrStore 90"
        )


    if answers["bot_type"] == "member":
        bot_type = (
            "follow 1\n"
            "route_randomWalk 0"
        )
    elif answers["bot_type"] == "leader":
        bot_type = (
            "follow 0\n"
            "route_randomWalk 1"
        )

    if answers["autoloot"] == "yes":
        autoloot = "cmdOnLogin c @autoloot"
    elif answers["autoloot"] == "no":
        autoloot = "# cmdOnLogin autoloot disabled"

    if answers["attack_behaviour"] == "aggresive":
        attack_behaviour = (
            "attackAuto 2\n"
            "attackAuto_party 1\n"
            "attackAuto_inLockOnly 1"
        )
    elif answers["attack_behaviour"] == "supportive":
        attack_behaviour = (
            "attackAuto 0\n"
            "attackAuto_party 1\n"
            "attackAuto_inLockOnly 1"
        )
    elif answers["attack_behaviour"] == "passive":
        attack_behaviour = (
            "attackAuto -1\n"
            "attackAuto_party 0\n"
            "attackAuto_inLockOnly 2"
        )


    if answers["follow_distance"] == "short":
        follow_distance = (
            "followDistanceMax 6\n"
            "followDistanceMin 3\n"
            "followLostStep 18\n"
            "followBot 0"
        )
    elif answers["follow_distance"] == "regular":
        follow_distance = (
            "followDistanceMax 10\n"
            "followDistanceMin 5\n"
            "followLostStep 18\n"
            "followBot 0"
        )
    elif answers["follow_distance"] == "long":
        follow_distance = (
            "followDistanceMax 20\n"
            "followDistanceMin 8\n"
            "followLostStep 18\n"
            "followBot 0"
        )


    if answers["arrows"] == "no":
        arrows = "# arrows disabled"
    elif answers["arrows"] == "yes":
        arrows = "!include ../../shared/buy_item/buy_arrows.txt"


    if answers["customSetMapLock"] == "yes":
        customSetMapLock = "customSetMapLock 1"
    elif answers["customSetMapLock"] == "no":
        customSetMapLock = "customSetMapLock 0"


    if answers["attackDistanceAuto"] == "yes":
        attackDistanceAuto = "attackDistanceAuto 1"
    elif answers["attackDistanceAuto"] == "no":
        attackDistanceAuto = "attackDistanceAuto 0"


    if answers["party_macro"] == "no":
        party_macro = "# party macro disabled"
    elif answers["party_macro"] == "1":
        party_macro = "!include ../../shared/party1.txt"
    elif answers["party_macro"] == "2":
        party_macro = "!include ../../shared/party2.txt"
    elif answers["party_macro"] == "3":
        party_macro = "!include ../../shared/party3.txt"


    if answers["aspd_potion"] == "no":
        aspd_potion = "# aspd potion disabled"
    elif answers["aspd_potion"] == "Concentration":
        aspd_potion = "!include ../../shared/use_item/potion_concentration.txt"
    elif answers["aspd_potion"] == "Awakening":
        aspd_potion = "!include ../../shared/use_item/potion_awakening.txt"
    elif answers["aspd_potion"] == "Berserk":
        aspd_potion = "!include ../../shared/use_item/potion_berserk.txt"


    if answers["default_heal_items"] == "no":
        default_heal_items = "# default heal disabled"
    elif answers["default_heal_items"] == "yes":
        default_heal_items = "!include ../../shared/use_item/heal_multi_heal.txt"


    if answers["customSetMaxPotion"] == "0":
        customSetMaxPotion = "customSetMaxPotion 0"
    elif answers["customSetMaxPotion"] == "1":
        customSetMaxPotion = "customSetMaxPotion 1"


    if answers["route_step"] == "15":
        route_step = "route_step 15"
    elif answers["route_step"] == "8":
        route_step = "route_step 8"
    elif answers["route_step"] == "5":
        route_step = "route_step 5"


    account = answers["account"]
    follow = answers["follow"]
    st_job = answers["st_job"]
    nd_job = answers["nd_job"]


    environment = Environment(loader=FileSystemLoader("./templates"))
    template1 = environment.get_template("config.tpl")
    template2 = environment.get_template("macros.tpl")

    content1 = template1.render(
        account=account,
        follow=follow,
        connection_type=connection_type,
        loot_action=loot_action,
        party_setup=party_setup,
        max_weight=max_weight,
        bot_type=bot_type,
        autoloot=autoloot,
        attack_behaviour=attack_behaviour,
        follow_distance=follow_distance,
        arrows=arrows,
        customSetMapLock=customSetMapLock,
        attackDistanceAuto=attackDistanceAuto,
        party_macro=party_macro,
        aspd_potion=aspd_potion,
        default_heal_items=default_heal_items,
        customSetMaxPotion=customSetMaxPotion,
        route_step=route_step,
        st_job=st_job,
        nd_job=nd_job,
        tldr=answers,
    )

    content2 = template2.render(
        party_macro=party_macro,
    )

    output_path = "./result/profiles/"

    others = [
        "items_control",
        "mon_control",
        "arrowcraft",
        "avoid",
        "eventMacros",
        "buyer_shop",
        "chat_resp",
        "consolecolors",
        "overallAuth",
        "pickupitems",
        "poseidon",
        "priority",
        "responses",
        "routeweights",
        "shop",
        "sys",
        "timeouts",
        "password",
    ]

    pathlib.Path(f"{output_path}{answers['account']}/").mkdir(parents=True, exist_ok=True)

    with open(
        f"{output_path}{answers['account']}/config.txt", mode="w+", encoding="utf-8"
    ) as message:
        message.write(f"{content1}\n")
        print("✓ Config saved!")

    with open(
        f"{output_path}{answers['account']}/macros.txt", mode="w+", encoding="utf-8"
    ) as message:
        message.write(f"{content2}\n")
        print("✓ Macro saved!")

    for other_config in others:
        template_x = environment.get_template(f"{other_config}.tpl")
        content_x = template_x.render()
        with open(
            f"{output_path}{answers['account']}/{other_config}.txt",
            mode="w+",
            encoding="utf-8",
        ) as message:
            message.write(f"{content_x}\n")
            print(f"✓ {other_config} saved!")
else:
    print(
        "slave-passive = do not attack anything\n"
        "master-aggresive = party leader\n"
        "slave-supportive = party member that will attack only monsters master fighting with master\n"
        "slave-aggresive = party member but aggresive"
        )
    p_template = [
        inquirer.List(
            "template",
            message="What preset to use",
            choices=["master-aggresive", "slave-passive", "slave-supportive", "slave-aggresive"],
        ),
    ]
    preset = inquirer.prompt(p_template)
