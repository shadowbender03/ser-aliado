# PROJECT_FIELD_NODE.md - The Portable Forge

## Objective
Migrate the Ser Aliado core to a Raspberry Pi 5 (8GB) to create an always-on, portable, independent field node.

## Target Date
March 2026

## Hardware Specs
- **Model:** Raspberry Pi 5 (8GB RAM)
- **Storage:** 128GB microSD (High Endurance preferred)
- **Cooling:** Active Cooler (Official or Argon)
- **Power:** 27W USB-C PD (Official Supply)

## Software Stack (The Migration)
1.  **OS:** Raspberry Pi OS (64-bit) / Ubuntu Server.
2.  **Core:** OpenClaw Gateway (Headless Mode).
3.  **Voice:** Piper TTS + `en_US-lessac-medium.onnx` (Low latency).
4.  **Tunnel:** Cloudflared (System Service) for permanent URL.
5.  **Logic:** `backend.py` (Flask) + `tokenizer.py` (Fluid Logic).

## Pre-Flight Checklist (Mac Phase)
- [x] Verify Piper TTS locally (Done).
- [x] Verify Cloudflare Tunnel (Done).
- [x] Verify Python Flask Backend (Done).
- [ ] Refine Tasker Handshake (Add Auth Token).
- [ ] Create `setup.sh` script for one-step Pi installation.

## Field Capabilities
- **24/7 Uptime:** No sleep mode. Always listening for Tasker.
- **Portable:** Can run on a USB-C battery bank in the shop or Panama.
- **Sovereign:** Does not rely on the MacBook Air being open.

## Migration Protocol
1.  **Flash:** Burn OS to SD card.
2.  **Clone:** Pull `ser-aliado` repo from GitHub.
3.  **Install:** Run `setup.sh` (install dependencies, brew/apt).
4.  **Transfer:** Copy `.env` and `credentials` securely (manual transfer).
5.  **Ignite:** Start services (`systemd`).

*Status: Pending Hardware. Blueprint Sealed.* 📦🛠️
