#!/bin/bash

file="$1"

if [[ ! -f "$file" ]]; then
  echo "File not found: $file"
  exit 1
fi

file_type=$(file -b --mime-type "$file")

case "$file_type" in
"application/zip"*)
  unzip "$file" || echo "Error extracting $file (unzip)"
  ;;
"application/gzip"*) # .tar.gz or .tgz
  tar -xzf "$file" || echo "Error extracting $file (tar xzf)"
  ;;
"application/x-bzip2"*) # .tar.bz2 or .tbz2
  tar -xjf "$file" || echo "Error extracting $file (tar xjf)"
  ;;
"application/x-xz"*)                                        # .tar.xz or .txz
  tar -xf "$file" || echo "Error extracting $file (tar xf)" # or tar -xf if xz is not installed
  ;;
"application/x-rar-compressed"*)
  unrar e "$file" || echo "Error extracting $file (unrar)"
  ;;
"application/x-7z-compressed"*)
  7z x "$file" || echo "Error extracting $file (7z)"
  ;;
*) # Default fallback
  echo "Unknown archive type: $file_type.  Try extracting manually."
  ;;
esac
