#!/bin/bash

read -p "Enter directory name: " dirname

if [[ -z "$dirname" ]]; then
  echo "Directory name cannot be empty."
  exit 1
fi

mkdir "$dirname"