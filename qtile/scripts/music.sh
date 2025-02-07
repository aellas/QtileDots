#!/bin/sh
playerctl metadata --format "{{artist}} - {{title}}" 2>/dev/null || echo "No music"