import os.path


def show_requirements_txt():
    requirement_text_path = os.path.join(
        os.getcwd(),
        'requirements.txt'
    )
    with open(requirement_text_path) as f:
        requirements_txt_content = f.read()
    print(requirements_txt_content)
