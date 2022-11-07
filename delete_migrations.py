from pathlib import Path


def main():
    app_folder = Path() / "app_dir" # The directory where your apps are located, work fine with cookiecutter-django projects 
    for folder in app_folder.iterdir():
        migration_folder = folder / "migrations"
        if migration_folder.exists():
            for file in migration_folder.iterdir():
                if str(file).endswith(".py") and (
                    not str(file).split("/")[-1].startswith("__")
                ):
                    file.unlink()
                    print(f"{str(file)} deleted")


if __name__ == "__main__":
    main()
