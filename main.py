# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open("Input/Letters/starting_letter.txt", "r") as letter:
    contents = letter.read()
    letter.close()

with open("Input/Names/invited_names.txt", "r") as names:
    name_list = []
    for name in names:
        name_strip = name.strip()
        name_list.append(name_strip)
    names.close()

for a_name in name_list:
    named_letter = contents.replace("[name]", a_name)
    ready_letter = open(f"Output/ReadyToSend/{a_name}_letter.txt", "w+")
    ready_letter.write(named_letter)
    ready_letter.close()
