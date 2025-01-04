# Convert from normal to brainrot
brainrot = (input("Enter text: \n")).lower()

replacements = {
    "hawk tuah": "blowjob",
    "talk tuah": "talk to her",
    "deez nuts": "these balls",
    "john pork": "hybrid pig-human",
    "nuh uh": "no"
}

for replacement, original in replacements.items():
    brainrot = brainrot.replace(replacement, original)

brainrot = brainrot.split(" ")

transformations = {
    "huzz": "women",
    "bruzz": "bro",
    "unempluzz": "unemployed",
    "duzz": "dad",
    "muzz": "mom",
    "brainruzz": "brainrot",
    "gruzz": "grandma",
    "chuzz": "ugly women",
    "tiktuzz": "tiktok",
    "tuzz": "teacher",
    "fuzz": "freshman",
    "rizzler": "charming guy",
    "ahh": "ass",
    "edging": "holding their orgasm",
    "gooning": "jerking off",
    "jorking": "jerking off",
    "jelqing": "",
    "sus": "suspicious",
    "irl": "in real life",
    "sigma": "",
    "alpha": "dominant",
    "blud": "blood",
    "dawg": "dog",
    "schlawg": "dog",
    "schnawg": "dog",
    "bussing": "good",
    "goofy": "weird",
    "chungus": "large",
    "zesty": "gay",
    "glizzy": "penis",
    "meat": "penis",
    "schlong": "penis",
    "wood": "penis",
    "pp": "penis",
    "mewing": "improving facial structure",
    "gigachad": "muscular and attractive man",
    "fr": "for real",
    "lockin": "focus",
    "bop": "whore",
    "cooked": "defeated",
    "cooking": "winning",
    "grind": "working hard",
    "opp": "enemy",
    "yn": "young nigga",
    "unc": "uncle",
    "yunc": "young nigga uncle",
    "yap": "talking a lot",
    "yapping": "talking excessively"
}

for i in range(len(brainrot)):
    for original, transformed in transformations.items():
        if brainrot[i] == transformed:
            brainrot[i] = original

output = ' '.join(brainrot)

print(output)