#!/bin/bash

read -p "Enter filename: " filename

if [[ -z "$filename" ]]; then
  echo "Filename cannot be empty."
  exit 1
fi

touch "$filename"