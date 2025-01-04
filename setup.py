from cx_Freeze import setup, Executable

# Define the script to be converted into an executable
script = "send_whatsapp_message.py"  # Name of your script file

# Build options
build_options = {
    "packages": ["selenium", "time", "os"],  # Add any additional required packages
    "excludes": [],  # List of modules to exclude if necessary
    "include_files": ["chromedriver.exe", "config.json"]  # List of files to include (e.g., additional assets, configuration files)
}

# Define the executable
executable = Executable(
    script,  # Script file to build into executable
    base="Console",  # Use 'Console' for a console application (use 'Win32GUI' for GUI applications)
    target_name="whatsapp_automation.exe"  # Desired name of the .exe file
)

# Setup function to create the executable
setup(
    name="Whatsapp Automation",
    version="1.0",
    description="Automate WhatsApp Web message sending",
    options={"build_exe": build_options},
    executables=[executable]
)
