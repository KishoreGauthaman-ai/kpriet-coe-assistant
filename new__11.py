import json

# Load dictionary
with open("place_phone_dict.json", "r", encoding="utf-8") as f:
    place_phone_dict = json.load(f)

# Update values in the same dictionary
for place, phone in place_phone_dict.items():
    place_phone_dict[place] = phone.replace(" ", "").replace("+91", "")

# Save back to the same file
with open("place_phone_dict.json", "w", encoding="utf-8") as f:
    json.dump(place_phone_dict, f, ensure_ascii=False, indent=4)

print("Phone numbers updated successfully.")