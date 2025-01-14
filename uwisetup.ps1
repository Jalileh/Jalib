
# CHOCO INSTALLER
# RUN THIS BEFORE THE SCRIPT --> Set-ExecutionPolicy Bypass -Scope Process -Force

if (-not (Get-Command choco -ErrorAction SilentlyContinue)) {
    Write-Host "Chocolatey is not installed. Installing now..."
    Set-ExecutionPolicy Bypass -Scope Process -Force
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
    iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
    
} else {
    Write-Host "Chocolatey is already installed."
}

choco install nerd-fonts-firacode -y

./essentials/tools/choco-installs.ps1

git clone 'https://github.com/Jalileh/shell'
git clone 'https://github.com/Jalileh/git-automation'




# pov your pc is too shit for WSL
$BASH = "C:\Program Files\Git\bin"; 
$Target = [System.EnvironmentVariableTarget]::User
[System.Environment]::SetEnvironmentVariable('Path', $env:Path + ";$BASH", $Target)

git config --global user.name "Jalileh"
git config --global user.email yacoub.m94f@gmail.com

py init_env_scripts.py
py init_bash_config.py

py init_text_editor_configs.py

