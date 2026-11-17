from functions.get_files_info import get_files_info


def show(label: str, result: str) -> None:
    print(f"Result for {label}:")
    for line in result.split("\n"):
        print(f"  {line}")


show("current directory", get_files_info("calculator", "."))
show("'pkg' directory", get_files_info("calculator", "pkg"))
show("'/bin' directory", get_files_info("calculator", "/bin"))
show("'../' directory", get_files_info("calculator", "../"))
