# handles all the automated adding of another script (adding to setup.py, adding script file to scripts/, and adding .py file to main folder
import os

IGNORE_DIRECTORIES = ['.git', '.github',
                      '__pycache__', 'scripts', 'helper_automation']

if __name__ == "__main__":
    abs_path = os.path.dirname(os.path.abspath(__file__))
    pkg_path = abs_path.replace('/helper_automation', '')

    script_name = input(
        "Enter the name of the script you want to create (seperated by hyphen): ")

    os.system(f'mkdir {pkg_path}/scripts')

    # copy script template to scripts directory as correct name
    os.system(
        f'cp {abs_path}/script_template {pkg_path}/scripts/{script_name}')

    # BUG - FOR SOME REASON CALLING FROM THIS DIRECTORY RETURNS FALSE WHEN ASKING IF ANYTHING IS A DIRECTORY (seems like a python bug but maybe this is intentional for some god forsaken reason); will just have to move the file manually for now
    dirs = [
        d for d in os.listdir(pkg_path)
        if os.path.isdir(d) and d not in IGNORE_DIRECTORIES]

    # copy module template to package directory
    if len(dirs) == 1:
        # add to package directory
        os.system(
            f"cp {abs_path}/module_template.py {pkg_path}/{dirs[0]}/{script_name.replace('-', '_')}.py")
    else:
        # just copy in the current directory with the right name
        os.system(
            f"cp {abs_path}/module_template.py {script_name.replace('-', '_')}.py")
        print(
            f"""Couldn't automatically determine your package's directory (most likely due to a known bug). Consider adding one of {dirs} to the IGNORE_DIRECTORIES in the pip-boilerplate repo.
                But for now we created a copy file in the current directory for you to paste into your package directory.
            """)
