import argparse
import os
import zipfile

import inquirer
import requests


def download_template_to_dir(template_url: str, project_name: str) -> None:
    template_name: str = template_url.split("/")[-5]
    zip_name: str = template_name + ".zip"
    r: requests.Response = requests.get(template_url)

    with open(zip_name, "wb") as f:
        f.write(r.content)

    with zipfile.ZipFile(zip_name, "r") as zip_ref:
        zip_ref.extractall(".")

    os.remove(zip_name)
    os.rename(template_name + "-main", project_name)


def get_template_url(template: str) -> str:
    url_start: str = "https://codeload.github.com/Xarithma/"
    url_to_template: dict = {
        "First-person template": "GodotFirstPersonTemplate",
        "Third-person template": "GodotThirdPersonTemplate",
    }
    url_end: str = "/zip/refs/heads/main"

    return url_start + url_to_template[template] + url_end


def create_project_from_template(template: str, project_name: str) -> None:
    template_url = get_template_url(template)
    download_template_to_dir(template_url, project_name)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="A simple tool to start Godot projects.",
    )
    parser.add_argument(
        "--name",
        help="Specify project name",
    )
    parser.add_argument(
        "--features",
        nargs="*",
        help="Specify project features",
    )
    parser.add_argument(
        "--template",
        help="Specify project template",
    )

    args: argparse.Namespace = parser.parse_args()

    name: str = args.name
    template: str = args.template

    questions: list = []

    if not name:
        questions.append(inquirer.Text("name", message="Enter project name:"))

    if not template:
        questions.append(
            inquirer.List(
                "template",
                message="Select template:",
                choices=["First-person template", "Third-person template"],
            )
        )

    if questions:
        answers = inquirer.prompt(questions)
        name = answers.get("name", name)
        template = answers.get("template", template)

    print(f"Creating project with name {name}...")
    print(f"Downloading template {template}...")
    create_project_from_template(template, name)
    print("\n")
    print("Done!")
    print("\n")
    print("If you have Godot installed to path, run it with:")
    print("\n")
    print(f"  cd {name}")
    print("  godot project.godot")
    print("\n")


if __name__ == "__main__":
    main()
