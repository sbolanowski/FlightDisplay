#!/bin/bash

usage() {
    echo "Usage: $0 [--width WIDTH] [--height HEIGHT] [--theme THEME]"
    echo ""
    echo "Options:"
    echo "  --w WIDTH       Width of the window (default: 1000)"
    echo "  --h HEIGHT      Height of the window (default: 600)"
    echo "  --theme THEME   Choose the theme ('light' or 'dark', default: 'light')"
    echo "  --help          Show this help message"
    echo ""
    exit 1
}

if [[ "$1" == "--help" ]]; then
    usage
fi

WIDTH=1000
HEIGHT=600
THEME="light"  # Default theme

while [[ $# -gt 0 ]]; do
    case $1 in
        --w)
            WIDTH=$2
            if ! [[ "$WIDTH" =~ ^[0-9]+$ ]]; then
                echo "Error: The value for --width must be a positive integer."
                usage
            fi
            shift 2
            ;;
        --h)
            HEIGHT=$2
            if ! [[ "$HEIGHT" =~ ^[0-9]+$ ]]; then
                echo "Error: The value for --height must be a positive integer."
                usage
            fi
            shift 2
            ;;
        --theme)
            THEME=$2
            if [[ "$THEME" != "light" && "$THEME" != "dark" ]]; then
                echo "Error: Invalid theme. Please choose 'light' or 'dark'."
                usage
            fi
            shift 2
            ;;
        *)
            echo "Error: Unknown option: $1"
            usage
            ;;
    esac
done

exec python3 main.py --w $WIDTH --h $HEIGHT --theme $THEME