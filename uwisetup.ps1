
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

./essentials/tools/choco-installs.ps1

git clone 'https://github.com/Jalileh/shell'
git clone 'https://github.com/Jalileh/git-automation'

py init_env_scripts.py
py init_bash_config.py

init_text_editor_configs.py

