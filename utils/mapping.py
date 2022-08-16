import json

def flatten(source: dict, prefix=None) -> dict:

    '''
    Turn an arbitrarily structured object into a flat dictionary with dot-delimited full-path keys
    '''

    flattened = {}

    for key, value in source.items():
        key_path = key if prefix is None else prefix + "." + key
        if isinstance(value, dict):
            flattened.update(flatten(value, prefix=key_path))
        else:
            flattened[key_path] = value

    return flattened


def unflatten(source: dict, prefix=None) -> dict:
    '''
    Turn a flat dictionary with dot-delimited full-path keys into an arbitrarily structured object
    '''

    unflattened = {}

    def create(parent, key_path, value):

        if len(key_path) == 1:
            parent[key_path[0]] = value
        else:
            if key_path[0] not in parent:
                parent[key_path[0]] = {}
            create(parent[key_path[0]], key_path[1:], value)

    for key, value in source.items():
        key_path = key.split(".")
        create(unflattened, key_path, value)

    return unflattened


def apply_mapping(source: dict, rules: list, flatten_output=False) -> dict:

    def matches(query: str, obj):
        if not (isinstance(obj, list) or isinstance(obj, set)):
            obj = [obj]
        if query[-1] == "*":
            for entry in obj:
                if entry.startswith(query[:-2]):
                    return True
        else:
            if query in obj:
                return True
        return False

    target_set = {}

    source = flatten(source)

    for (rule_source, rule_target) in rules:

        if rule_source in source:
            # Rule path matches key exactly: write existing value under new keys
            target_set[rule_target] = source[rule_source]
        else:
            rule_path = rule_source.split(".")
            rule_prefix = ".".join(rule_path[:-1])  # Everything up to last part of path
            rule_suffix = rule_path[-1]  # Last part of path

            if rule_prefix in source and source[rule_prefix] is not None and matches(rule_suffix, source[rule_prefix]):
                #  Rule path matches key and value: write True under new keys
                target_set[rule_target] = True

            else:

                for key, value in source.items():

                    key_path = key.split(".")

                    if key_path[:len(rule_path)] == rule_path:

                        remainder = key_path[len(rule_path):]
                        target_path = rule_target.split(".")
                        target_set[".".join(target_path + remainder)] = value

    if flatten_output:
        return target_set
    else:
        return unflatten(target_set)


def map_few_hot(source: dict, rules: list) -> list:
    mapped_targets = apply_mapping(source, rules, flatten_output=True)
    one_hot = [1 if target in mapped_targets and mapped_targets[target] else 0 for target in unique_targets(rules)]
    return one_hot


def unique_targets(rules: list):
    return sorted(list(set([rule[1] for rule in rules])))


def expand_values(mapping: dict) -> list:

    # Expand a dictionary, which may contain arrays as values, into a 1-to-1 list with possible duplicate keys

    expanded_mapping = []
    for key, value in mapping.items():
        if not isinstance(value, list):
            value = [value]
        for sub_value in value:
            expanded_mapping.append((key, sub_value))

    return expanded_mapping

'''
if __name__ == "__main__":

    original = (
        {
            "A": "Value A",
            "B": {
                "A": "Value A",
                "B": "Value B",
                "C": {
                    "D": "Value D"
                },
                "E": {
                    "E": "Value E",
                    "F": "Value F"
                }
            }
        }
    )

    flattened = flatten(original)  # print(json.dumps(flattened, indent=4, sort_keys=True))
    unflattened = unflatten(flattened)  # print(json.dumps(unflattened, indent=4, sort_keys=True))
    assert unflattened == original

    mapped = many_map(
        original,
        {
            "A.B.Value B": "mapped.1",
            "B.E": "mapped.2"
        }
    )

    print(json.dumps(mapped, indent=4, sort_keys=True))
'''
