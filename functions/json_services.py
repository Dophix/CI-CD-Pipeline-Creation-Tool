import json

def create_json_template(json_data, project_name: str):
    with open("output/" + project_name + "-template.json", 'w') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)
        f.close()

