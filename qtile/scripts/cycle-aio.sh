#!/bin/bash
# ~/scripts/cycle-aio.sh

STATE_FILE="/tmp/aio_mode"
MODES=("quiet" "balanced" "extreme")

# Read current mode or default to "quiet"
if [[ -f $STATE_FILE ]]; then
    current_mode=$(<"$STATE_FILE")
else
    current_mode="quiet"
fi

# Find index of current mode
for i in "${!MODES[@]}"; do
    if [[ "${MODES[$i]}" == "$current_mode" ]]; then
        current_index=$i
        break
    fi
done

# Calculate next mode
next_index=$(( (current_index + 1) % ${#MODES[@]} ))
next_mode=${MODES[$next_index]}

# Call original script with new mode
~/scripts/aio.sh -m "$next_mode"

# Save new mode
echo "$next_mode" > "$STATE_FILE"

# Optional: send notification (requires `notify-send`)
notify-send "AIO Mode" "$next_mode"
