#!/usr/bin/env bash
set -e

# VoiceStudio runner script
export PATH="$HOME/.local/bin:$HOME/.bun/bin:$PATH"
export UV_OFFLINE=1
export UV_NO_SYNC=1

MODE="${1:-web}"

case "$MODE" in
  web)
    echo "Starting VoiceStudio in Web mode (Backend :3900, UI :3901)..."
    bun run dev:web
    ;;
  desktop)
    echo "Starting VoiceStudio Desktop app..."
    bun run dev
    ;;
  api)
    echo "Starting VoiceStudio Backend API (:3900)..."
    bun run dev:api
    ;;
  *)
    echo "Usage: ./start.sh [web|desktop|api]"
    exit 1
    ;;
esac

