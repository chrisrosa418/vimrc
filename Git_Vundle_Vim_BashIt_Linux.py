#Check to See if GIT is installed
from subprocess import Popen, PIPE
import os

#Fresh Install 
update = "sudo apt-get update"
os.system(update)

#Install Git 
git = "sudo apt-get install git"
os.system(git)

#Install Vim 
vim = "sudo apt-get install vim"
os.system(vim)

#Install Vundle
vundle = "git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim"
os.system(vundle)

#Create .vimrc
vimrc = "wget -O ~/.vimrc wget https://raw.githubusercontent.com/chrisrosa418/vimrc/master/.vimrc"
os.system(vimrc)

#Install Command
install = "vim +PluginInstall +qall"
os.system(install)

#Clone Bash It
bashit = "git clone --depth=1 https://github.com/Bash-it/bash-it.git ~/.bash_it"
os.system(bashit)

#Install Command
bashinstall = "~/.bash_it/install.sh"
os.system(bashinstall)
