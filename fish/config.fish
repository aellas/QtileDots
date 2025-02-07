function fish_greeting
    sh .config/myfetch/myfetch.sh
end

starship init fish | source
alias update "sudo pacman -Syu"
alias install "sudo pacman -S"
alias unused "sudo pacman -Rns $(pacman -Qtdq)"
alias remove "sudo pacman -R"

fish_add_path $HOME/dotfiles/lf
set -gx EDITOR nvim
set -gx VISUAL nvim


# Created by `pipx` on 2025-02-07 12:05:10
set PATH $PATH /home/array/.local/bin
