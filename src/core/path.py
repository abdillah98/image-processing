import os

def image_path(image_name):
    base_path = os.path.dirname(__file__)
    project_root = os.path.abspath(os.path.join(base_path, "..", ".."))
    input_path = os.path.join(project_root, "data", "input", image_name)
    return input_path