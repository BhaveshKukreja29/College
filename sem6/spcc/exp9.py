def pass1(source):
    mnt = []
    mdt = []
    ala = []
    intermediate = []
    i = 0

    while i < len(source):
        line = source[i].strip()

        if line == 'MACRO':
            i += 1
            proto = source[i].strip()
            parts = proto.replace(',', ' ').split()

            # first token may be &LAB, then macro name, then args
            formal_params = []
            macro_name = None
            for p in parts:
                if p.startswith('&'):
                    formal_params.append(p)
                elif macro_name is None:
                    macro_name = p

            ala_entry = {param: f"#{idx}" for idx, param in enumerate(formal_params)}

            mnt.append({'name': macro_name, 'mdt_index': len(mdt) + 1})

            # store prototype in MDT
            mdt_line = proto
            for param, idx in ala_entry.items():
                mdt_line = mdt_line.replace(param, idx)
            mdt.append(mdt_line)

            i += 1
            while i < len(source) and source[i].strip() != 'MEND':
                body_line = source[i].strip()
                for param, idx in ala_entry.items():
                    body_line = body_line.replace(param, idx)
                mdt.append(body_line)
                i += 1
            mdt.append('MEND')
            ala.append({'macro': macro_name, 'params': formal_params})
            i += 1
        else:
            intermediate.append(line)
            i += 1

    return mnt, mdt, ala, intermediate


def pass2(intermediate, mnt, mdt, ala):
    output = []

    for line in intermediate:
        parts = line.replace(',', ' ').split()
        macro_entry = None
        macro_call_parts = None

        for entry in mnt:
            if entry['name'] in parts:
                macro_entry = entry
                macro_call_parts = parts
                break

        if macro_entry is None:
            output.append(line)
        else:
            name = macro_entry['name']
            name_idx = parts.index(name)

            # collect actual params: label (if before name) + args after name
            actual_params = []
            if name_idx > 0:
                actual_params.append(parts[name_idx - 1])  # label
            else:
                actual_params.append('')
            actual_params.extend(parts[name_idx + 1:])

            # find ALA entry for this macro
            ala_entry = None
            for a in ala:
                if a['macro'] == name:
                    ala_entry = a
                    break

            # expand from MDT (skip prototype, stop before MEND)
            mdt_start = macro_entry['mdt_index']  # 1-indexed, prototype
            idx = mdt_start  # skip prototype line
            while idx < len(mdt) and mdt[idx] != 'MEND':
                expanded = mdt[idx]
                for j in range(len(actual_params)):
                    expanded = expanded.replace(f"#{j}", actual_params[j])
                output.append(expanded)
                idx += 1

    return output


# --- input ---
print("Enter source program (type 'END' on a new line to finish):")
source = []
while True:
    line = input()
    if line.strip() == 'END':
        break
    source.append(line)

mnt, mdt, ala, intermediate = pass1(source)

print("\n===== PASS 1 OUTPUT =====")

print("\nMacro Name Table (MNT):")
print(f"  {'Index':<8}{'Name':<12}{'MDT Index'}")
for i, entry in enumerate(mnt):
    print(f"  {i + 1:<8}{entry['name']:<12}{entry['mdt_index']}")

print("\nMacro Definition Table (MDT):")
print(f"  {'Index':<8}{'Definition'}")
for i, line in enumerate(mdt):
    print(f"  {i + 1:<8}{line}")

print("\nArgument List Array (ALA):")
for entry in ala:
    print(f"  Macro: {entry['macro']}")
    for i, p in enumerate(entry['params']):
        print(f"    #{i} -> {p}")

print("\nIntermediate Code (after removing macro defs):")
for line in intermediate:
    print(f"  {line}")

expanded = pass2(intermediate, mnt, mdt, ala)

print("\n===== PASS 2 OUTPUT =====")
print("\nExpanded Source Program:")
for line in expanded:
    print(f"  {line}")
