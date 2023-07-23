import sys
import os
import subprocess
import shutil

sys.path.append("../dependencies/dev_scripts")

from build_ark import build_patch_ark
from download_mackiloha import download_mackiloha

# List of required packages
required_packages = ["psutil"]

# Check if each package is installed, and if not, install it
for package in required_packages:
    try:
        import psutil
    except ImportError:
        print(f"{package} not found. Installing...")
        subprocess.check_call(["pip", "install", package])

def run_in_detached_process(command):
    # Start the command in a new subprocess with DETACHED_PROCESS flag
    subprocess.Popen(command, creationflags=subprocess.DETACHED_PROCESS, close_fds=True)


def close_rpcs3_process():
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == 'rpcs3.exe':
            print(f"Terminating rpcs3.exe (PID: {process.info['pid']})")
            process.terminate()
            process.wait()  # Wait for the process to terminate
            break

# Function to ask for the rpcs3 dev_hdd0 directory and save it to a file
def get_rpcs3_directory():
    directory_file = "rpcs3_directory.txt"
    if os.path.exists(directory_file):
        with open(directory_file, "r") as file:
            rpcs3_directory = file.readline().strip()
            if rpcs3_directory and validate_rpcs3_directory(rpcs3_directory):
                return rpcs3_directory
            else:
                print("Stored rpcs3_directory is not valid. Please enter the path again.")
                return input("Please enter the path to your rpcs3 dev_hdd0 directory: ")

    while True:
        rpcs3_directory = input("Please enter the path to your rpcs3 dev_hdd0 directory: ")
        if validate_rpcs3_directory(rpcs3_directory):
            with open(directory_file, "w") as file:
                file.write(rpcs3_directory)
            return rpcs3_directory
        else:
            print("Invalid directory. Please try again.")

def validate_rpcs3_directory(rpcs3_directory):
    game_folder_path = os.path.join(rpcs3_directory, "game")
    blus30463_folder_path = os.path.join(game_folder_path, "BLUS30463")

    if not os.path.exists(game_folder_path):
        print("Invalid directory: The 'game' folder is not found in the provided rpcs3 directory.")
        return False

    if not os.path.exists(blus30463_folder_path):
        print("Rock Band 3 (BLUS30463) not detected in the provided rpcs3 directory. Creating One.")
        os.makedirs(blus30463_folder_path, exist_ok=True)
        return True

    return True

rpcs3_directory = get_rpcs3_directory()

successful_extraction = download_mackiloha()

if successful_extraction:
    if build_patch_ark(False, rpcs3_directory, rpcs3_mode=True):
        close_rpcs3_process()

        # Copy files from _build/ps3 to rpcs3_directory/game/BLUS30463
        source_dir = "../_build/ps3"
        # Delete _build/ps3/USRDIR/gen folder if it exists
        gen_folder_path = os.path.join(source_dir, "USRDIR", "gen")
        if os.path.exists(gen_folder_path):
            shutil.rmtree(gen_folder_path)
        destination_dir = os.path.join(rpcs3_directory, "game", "BLUS30463")

        # Ensure destination_dir exists before copying
        os.makedirs(destination_dir, exist_ok=True)

        # Copy files
        for root, dirs, files in os.walk(source_dir):
            relative_path = os.path.relpath(root, source_dir)
            destination_path = os.path.join(destination_dir, relative_path)
            os.makedirs(destination_path, exist_ok=True)
            for file in files:
                source_file = os.path.join(root, file)
                destination_file = os.path.join(destination_path, file)
                shutil.copy2(source_file, destination_file)

        # Check for rpcs3.exe in the parent folder of rpcs3_directory
        rpcs3_exe_path = os.path.join(os.path.dirname(rpcs3_directory), "rpcs3.exe")
        discordrichpresence_path = os.path.join(os.path.dirname(__file__), "discordrichpresence.py")

        suffix = "_rpcs3" if os.path.exists(rpcs3_exe_path) else ""

        # Create the json_path file with the appropriate suffix
        json_path = os.path.join(rpcs3_directory, "game", "BLUS30463", "USRDIR", "discordrp.json")
        with open(f"json_path{suffix}.txt", "w") as file:
            file.write(json_path)

        # Run discordrichpresence.py with the appropriate suffix
        subprocess.Popen(["python", discordrichpresence_path, suffix])

        # Run rpcs3 with the appropriate suffix in a detached process
        eboot_bin_path = os.path.join(rpcs3_directory, "game", "BLUS30463", "USRDIR", "eboot.bin")
        run_in_detached_process([rpcs3_exe_path, eboot_bin_path])

    else:
        print("Error building PS3 ARK. Check your modifications or run git_reset.py to rebase your repo.")