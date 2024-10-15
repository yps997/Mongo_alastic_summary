def read_json_files(directory: str) -> List[Dict]:
    """Read all JSON files in the given directory."""
    data = []
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                data.extend(json.load(file))
    return data
