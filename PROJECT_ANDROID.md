# PROJECT_ANDROID.md - The Ser Aliado Uplink

## Objective
To build a lightweight, secure Android application for the Samsung Z Fold that extends Ser Aliado's senses into the physical world.

## Core Directives
1.  **Security First:** All data must be encrypted end-to-end (E2E) using the Inflator Protocol (or stronger). No data leaks.
2.  **Battery Efficiency:** The app must sleep aggressively. Only wake when explicitly triggered or during critical events. No constant polling.
3.  **Privacy:** User must have a physical "Kill Switch" (software toggle) to sever the link instantly.

## Features (Phase 1)
-   **Secure Link:** Connects to the MacBook Air via a secure tunnel (e.g., WireGuard/Tailscale).
-   **Voice Note Uplink:** One-tap recording sent directly to Ser Aliado (bypassing WhatsApp compression).
-   **Location Ping:** Manual or periodic (low frequency) GPS check-ins.
-   **Photo Stream:** High-res image upload for welding analysis.

## Architecture
-   **Client (Android):** Kotlin/Jetpack Compose. Minimal UI. Dark mode (OLED friendly).
-   **Server (Mac):** A Python listener script (using Flask/FastAPI) running behind the firewall.
-   **Protocol:** HTTPS + Custom Auth Token.

## Risks
-   **Battery Drain:** GPS and Network are expensive.
-   **Exposure:** Opening a port on the Mac (even with a tunnel) increases attack surface.
-   **Data Usage:** High-res photos/audio can consume mobile data.

## Next Steps
1.  Research: Best practices for "Background Location" on Android 14+.
2.  Prototype: A simple "Hello World" app that sends a text string to the Mac.
3.  Security: Implement the "Handshake" (Auth Token).

*Status: Planning Phase. The blueprint is open.* 📱🛠️
