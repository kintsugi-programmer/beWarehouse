# beWarehouse : Debian Daily Operations Cheat Sheet

## Table of Contents
- [beWarehouse : Debian Daily Operations Cheat Sheet](#bewarehouse--debian-daily-operations-cheat-sheet)
  - [Table of Contents](#table-of-contents)
  - [System Information](#system-information)
  - [Package Management](#package-management)
  - [User Management](#user-management)
  - [File System Operations](#file-system-operations)
  - [Network Operations](#network-operations)
  - [System Services](#system-services)
  - [System Logs](#system-logs)
  - [Git Configuration](#git-configuration)
  - [Python](#python)
  - [Environment Variables](#environment-variables)
  - [SSH](#ssh)
  - [OpenFortiVPN](#openfortivpn)
  - [Miscellaneous](#miscellaneous)
  - [REcent](#recent)
  - [System Update \& Upgrade](#system-update--upgrade)
  - [Install Required Packages](#install-required-packages)
  - [Visual Studio Code Extensions](#visual-studio-code-extensions)
  - [Clone \& Install auto-cpufreq](#clone--install-auto-cpufreq)
  - [Install Brave Browser](#install-brave-browser)
  - [Install Spotify](#install-spotify)
  - [Install Sublime Text](#install-sublime-text)
  - [Install TLDR](#install-tldr)
  - [Install Node.js and npm](#install-nodejs-and-npm)
  - [Add User to vboxusers Group](#add-user-to-vboxusers-group)


## System Information

- **Check Debian Version:**
  ```bash
  lsb_release -a
  ```
  
- **Check Kernel Version:**
  ```bash
  uname -r
  ```

- **Check System Uptime:**
  ```bash
  uptime
  ```

- **Check Disk Usage:**
  ```bash
  df -h
  ```

- **Check Memory Usage:**
  ```bash
  free -h
  ```

- **Check CPU Usage:**
  ```bash
  top
  ```

## Package Management

- **Update Package List:**
  ```bash
  sudo apt update
  ```

- **Upgrade All Packages:**
  ```bash
  sudo apt upgrade
  ```

- **Full System Upgrade:**
  ```bash
  sudo apt full-upgrade
  ```

- **Install a Package:**
  ```bash
  sudo apt install package-name
  ```

- **Remove a Package:**
  ```bash
  sudo apt remove package-name
  ```

- **Purge a Package (removes config files):**
  ```bash
  sudo apt purge package-name
  ```

- **Search for a Package:**
  ```bash
  apt search package-name
  ```

- **List Installed Packages:**
  ```bash
  dpkg -l
  ```

- **Check Package Details:**
  ```bash
  apt show package-name
  ```

- **Clean Up Unused Packages:**
  ```bash
  sudo apt autoremove
  ```

## User Management

- **Add a New User:**
  ```bash
  sudo adduser username
  ```

- **Delete a User:**
  ```bash
  sudo deluser username
  ```

- **Add User to a Group:**
  ```bash
  sudo usermod -aG groupname username
  ```

- **Change User Password:**
  ```bash
  sudo passwd username
  ```

## File System Operations

- **List Files in Directory:**
  ```bash
  ls -l
  ```

- **Change Directory:**
  ```bash
  cd /path/to/directory
  ```

- **Create a New Directory:**
  ```bash
  mkdir directory-name
  ```

- **Remove a Directory:**
  ```bash
  rmdir directory-name
  ```

- **Copy Files:**
  ```bash
  cp source-file destination-file
  ```

- **Move/Rename Files:**
  ```bash
  mv source-file destination-file
  ```

- **Remove Files:**
  ```bash
  rm file-name
  ```

## Network Operations

- **Check IP Address:**
  ```bash
  ip a
  ```

- **Check Network Connections:**
  ```bash
  ss -tuln
  ```

- **Ping a Host:**
  ```bash
  ping hostname-or-ip
  ```

- **Check Routing Table:**
  ```bash
  ip route
  ```

- **Restart Network Service:**
  ```bash
  sudo systemctl restart networking
  ```

## System Services

- **Check Service Status:**
  ```bash
  sudo systemctl status service-name
  ```

- **Start a Service:**
  ```bash
  sudo systemctl start service-name
  ```

- **Stop a Service:**
  ```bash
  sudo systemctl stop service-name
  ```

- **Restart a Service:**
  ```bash
  sudo systemctl restart service-name
  ```

- **Enable a Service to Start at Boot:**
  ```bash
  sudo systemctl enable service-name
  ```

- **Disable a Service from Starting at Boot:**
  ```bash
  sudo systemctl disable service-name
  ```

## System Logs

- **View System Logs:**
  ```bash
  journalctl -xe
  ```

- **View Specific Log File:**
  ```bash
  less /var/log/syslog
  ```

- **Tail a Log File:**
  ```bash
  tail -f /var/log/syslog
  ```

## Git Configuration

- **Set Global Git User Email & Name:**
  ```bash
    git config --global user.email "siddhant22496@iiitd.ac.in"
    git config --global user.name "kintsugi-warrior"
  ```

- **Check Git Configuration:**
  ```bash
  git config --list
  ```

- **Clone a Repository:**
  ```bash
  git clone repository-url
  ```

- **Check Status of Repository:**
  ```bash
  git status
  ```

- **Commit Changes:**
  ```bash
  git commit -m "commit message"
  ```

- **Push Changes to Remote:**
  ```bash
  git push
  ```

- **Pull Changes from Remote:**
  ```bash
  git pull
  ```

## Python

- **Check Python Version:**
  ```bash
  python --version
  ```
  
- **Check Python3 Version:**
  ```bash
  python3 --version
  ```

- **Install Python Package:**
  ```bash
  pip install package-name
  ```

- **Install Python3 Package:**
  ```bash
  pip3 install package-name
  ```

- **List Installed Python Packages:**
  ```bash
  pip list
  ```

- **Create Virtual Environment:**
  ```bash
  python -m venv env-name
  ```

- **Activate Virtual Environment:**
  ```bash
  source env-name/bin/activate
  ```

- **Deactivate Virtual Environment:**
  ```bash
  deactivate
  ```

## Environment Variables

- **Set Environment Variable Temporarily:**
  ```bash
  export VARIABLE_NAME=value
  ```

- **Set Environment Variable Permanently (in `.bashrc` or `.bash_profile`):**
  ```bash
  echo 'export VARIABLE_NAME=value' >> ~/.bashrc
  source ~/.bashrc
  ```

- **View Environment Variables:**
  ```bash
  printenv
  ```

## SSH

- **Generate SSH Key Pair:**
  ```bash
  ssh-keygen -t rsa -b 4096 -C "your-email@example.com"
  ```

- **Add SSH Key to SSH Agent:**
  ```bash
  eval "$(ssh-agent -s)"
  ssh-add ~/.ssh/id_rsa
  ```

- **Copy SSH Key to Clipboard:**
  ```bash
  cat ~/.ssh/id_rsa.pub
  ```

- **Connect to a Remote Host:**
  ```bash
  ssh username@hostname
  ```

- **View SSH Configuration:**
  ```bash
  cat ~/.ssh/config
  ```

## OpenFortiVPN

- **Install OpenFortiVPN:**
  ```bash
  sudo apt install openfortivpn
  ```

- **Connect to a VPN:**
  ```bash
  sudo openfortivpn -c /etc/openfortivpn/config
  ```
- **Connect to a IIITD :**
  ```bash
  sudo openfortivpn vpn.iiitd.edu.in:10443 --username=siddhant22496
  ```
- **Config file**
  ```bash
    sudo nano /etc/openfortivpn/config
    sudo chmod 600 /etc/openfortivpn/config
    sudo openfortivpn
  ```

    ```bash
    # OpenFortiVPN Configuration File

    host = vpn.iiitd.edu.in
    port = 10443
    username = siddhant22496
    # Uncomment the following line if you have a password file
    # password = /path/to/password-file
    # Optional: You can specify the VPN gateway, client certificate, etc.
    # gateway = vpn-gateway-address
    # client-cert = /path/to/client-cert.pem
    # client-key = /path/to/client-key.pem


    ```
- **Check OpenFortiVPN Status:**
  ```bash
  sudo systemctl status openfortivpn
  ```

- **Start OpenFortiVPN Service:**
  ```bash
  sudo systemctl start openfortivpn
  ```

- **Stop OpenFortiVPN Service:**
  ```bash
  sudo systemctl stop openfortivpn
  ```

- **Enable OpenFortiVPN Service to Start at Boot:**
  ```bash
  sudo systemctl enable openfortivpn
  ```

## Miscellaneous
- **Alias Setup:**
  ```bash
  nano ~/.bashrc
  ```
  ```bash
  alias shortcut_name='full_command'
  ```
  ```bash
  source ~/.bashrc
  ```

- **Reboot the System:**
  ```bash
  sudo reboot
  ```

- **Shutdown the System:**
  ```bash
  sudo shutdown -h now
  ```

- **Check for Broken Packages:**
  ```bash
  sudo apt --fix-broken install
  ```

- **Check Disk Space Usage:**
  ```bash
  sudo du -sh /path/to/directory
  ```
## REcent
```bash
#!/bin/bash

# Clear terminal
clear

# List contents of the current directory
ls
ls -R
clear

# Install necessary packages
sudo apt update
sudo apt install -y curl neofetch build-essential code git-all lolcat htop golang qbittorrent mysql-server sublime-text libreoffice pix audacious ghostwriter github-desktop virtualbox virtualbox-ext-pack tree fd-find exa duf cheese

# Install Brave browser
sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg] https://brave-browser-apt-release.s3.brave.com/ stable main" | sudo tee /etc/apt/sources.list.d/brave-browser-release.list
sudo apt update
sudo apt install brave-browser -y

# Set opacity for Visual Studio Code
bash -c 'for W in $(wmctrl -l |grep "Visual Studio Code" |awk '\''{print $1}'\''); do xprop -id $W -format _NET_WM_WINDOW_OPACITY 32c -set _NET_WM_WINDOW_OPACITY $(printf 0x%x $((0xffffffff * 97 / 100))); done'

# Git configuration
git config --global user.email "siddhant22496@iiitd.ac.in"
git config --global user.name "kintsugi-warrior"

# Install OpenFortiVPN and connect
sudo apt install -y openfortivpn
sudo openfortivpn vpn.iiitd.edu.in:10443 --username=siddhant22496
sudo chmod 600 /etc/openfortivpn/config
openfortivpn

# Clone GitHub repository
gh repo clone kintsugi-programmer/balisalgo
git clone https://github.com/kintsugi-programmer/balisalgo.git

# Install GitHub CLI
(type -p wget >/dev/null || (sudo apt update && sudo apt-get install wget -y)) 
sudo mkdir -p -m 755 /etc/apt/keyrings 
wget -qO- https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null 
sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg 
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null 
sudo apt update 
sudo apt install gh -y

# Compile and run C++ code
cd "/home/kintsugi-warrior/BaliGit/balisalgo/CodeRunner/" && g++ code.cpp -o code && "./code"
cd "/home/kintsugi-warrior/BaliGit/balisalgo/cpp/" && g++ cppprac.cpp -o cppprac && "./cppprac"
cd "/home/kintsugi-warrior/BaliGit/balisalgo/patterns/" && g++ prac.cpp -o prac && "./prac"

# Update and upgrade the system
sudo apt update && sudo apt upgrade -y

# Install g++
sudo apt install g++ -y

# Re-run C++ code after g++ installation
cd "/home/kintsugi-warrior/BaliGit/balisalgo/CodeRunner/" && g++ code.cpp -o code && "./code"
cd "/home/kintsugi-warrior/BaliGit/balisalgo/" && g++ code.cpp -o code && "./code"

# Bashrc modifications and source
nano ~/.bashrc
source ~/.bashrc

# Connect to IIITD VPN
iiitd

# Set opacity for Visual Studio Code (multiple times)
bash -c 'for W in $(wmctrl -l |grep "Visual Studio Code" |awk '\''{print $1}'\''); do xprop -id $W -format _NET_WM_WINDOW_OPACITY 32c -set _NET_WM_WINDOW_OPACITY $(printf 0x%x $((0xffffffff * 97 / 100))); done'

```

## System Update & Upgrade

```bash
echo "Updating and upgrading system..."
sudo apt update && sudo apt upgrade -y
```

## Install Required Packages

```bash
echo "Installing required packages..."
sudo apt install -y neofetch build-essential code git-all curl lolcat htop golang qbittorrent mysql-server sublime-text libreoffice pix audacious ghostwriter github-desktop virtualbox virtualbox-ext-pack tree fd-find exa duf cheese
```

## Visual Studio Code Extensions

```bash
echo "Installing Visual Studio Code extensions..."
code --install-extension ahmadawais.shades-of-purple \
     --install-extension CoenraadS.bracket-pair-colorizer-2 \
     --install-extension eamodio.gitlens \
     --install-extension dbaeumer.vscode-eslint \
     --install-extension esbenp.prettier-vscode \
     --install-extension ritwickdey.LiveServer \
     --install-extension msjsdiag.debugger-for-chrome \
     --install-extension ms-azuretools.vscode-docker \
     --install-extension ms-vscode-remote.remote-ssh \
     --install-extension ms-vscode.cpptools \
     --install-extension formulahendry.code-runner \
     --install-extension Zackptg5.Glassit \
     --install-extension ms-toolsai.jupyter \
     --install-extension vscjava.vscode-maven \
     --install-extension mtxr.sqltools \
     --install-extension ms-python.python \
     --install-extension donjayamanne.githistory \
     --install-extension vscodevim.vim \
     --install-extension dsznajder.es7-react-js-snippets \
     --install-extension esbenp.prettier-vscode \
     --install-extension ecmel.vscode-html-css \
     --install-extension GitHub.copilot
```

## Clone & Install auto-cpufreq

```bash
echo "Installing auto-cpufreq..."
git clone https://github.com/AdnanHodzic/auto-cpufreq.git
cd auto-cpufreq && sudo ./auto-cpufreq-installer
cd ..
```

## Install Brave Browser

```bash
echo "Installing Brave browser..."
sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg] https://brave-browser-apt-release.s3.brave.com/ stable main" | sudo tee /etc/apt/sources.list.d/brave-browser-release.list
sudo apt update
sudo apt install -y brave-browser
```

## Install Spotify

```bash
echo "Installing Spotify..."
curl -sS https://download.spotify.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb http://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list
sudo apt update
sudo apt install -y spotify-client
```

## Install Sublime Text

```bash
echo "Installing Sublime Text..."
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
sudo apt-add-repository "deb https://download.sublimetext.com/ apt/stable/"
sudo apt update
sudo apt install -y sublime-text
```

## Install TLDR

```bash
echo "Installing TLDR..."
sudo apt install -y tldr
sudo tldr --update
```

## Install Node.js and npm

```bash
echo "Installing Node.js and npm..."
curl -sL https://deb.nodesource.com/setup_14.x | sudo bash -
sudo apt-get install -y nodejs npm
```

## Add User to vboxusers Group

```bash
echo "Adding user to vboxusers group..."
sudo usermod -aG vboxusers $USER
```

