def skaits(vārds):
    if len (vārds)<5:
        response ="īss"
    elif len (vārds)<10:
        response = "vidējias"
    else:
        response = "garš"

    print(f"Vārdam '{vārds}' garums ir {response}")

skaits("skaidrins")