---
id: gemini_0503598e9b43019e
title: Resetting Odysseus AI Admin Password
source: gemini
url: "https://gemini.google.com/app/0503598e9b43019e"
created: "2026-10-04T12:53:50+08:00"
modified: "2026-10-04T12:53:50+08:00"
tags:
  - ai-conversation
  - gemini
message_count: 6
---

> [!QUESTION] User
> In odysseus ai (https://github.com/odysseus-dev/odysseus). I forgot my admin password. Can you help me troubleshoot how to retrieve it?

> [!NOTE] Gemini
> In **Odysseus AI**, the admin password cannot be recovered in plaintext once it has been generated because the application stores a cryptographic hash of it inside the `data/auth.json` file. Furthermore, environment variables like `ODYSSEUS_ADMIN_PASSWORD` only act as a one-time bootstrap on the initial setup.
> 
> GitHub
> 
> If you have lost or forgotten your password and cannot log in, you can reset it by forcing Odysseus to regenerate a new authentication file. Follow the steps below based on how you installed Odysseus:
> 
> ### Method 1: If running via Docker (Recommended)
> 
> 1.  Stop the running containers:
>     
>     Bash
>     
>     ```
>     docker compose down
>     ```
>     
> 2.  Delete or move the existing authentication file (`data/auth.json`) located inside your Odysseus data directory:
>     
>     Bash
>     
>     ```
>     rm data/auth.json
>     ```
>     
>     *(Note: If you don't do this, Docker will reuse the existing `auth.json` and will not print a new temporary password).*
>     
> 3.  Start the containers back up:
>     
>     GitHub
>     
>     Bash
>     
>     ```
>     docker compose up -d --build
>     ```
>     
> 4.  View the container logs to copy the newly generated temporary admin password:
>     
>     Bash
>     
>     ```
>     docker compose logs odysseus
>     ```
>     
>     Look through the output for the line displaying `Temporary password:`. Use that password along with the default username (`admin` unless you explicitly changed `ODYSSEUS_ADMIN_USER`) to log into `http://localhost:7000`.
>     
> 
> ### Method 2: If running locally via Python/Source
> 
> 1.  Stop your running Odysseus server terminal session (`Ctrl + C`).
>     
> 2.  Delete the `auth.json` file inside your data folder:
>     
>     Bash
>     
>     ```
>     rm data/auth.json
>     ```
>     
> 3.  Re-run your setup script (`python setup.py` or your standard startup command).
>     
> 4.  The terminal will output a brand-new temporary admin password upon recreation. Copy it and log back in.
>     
> 
> *(Once logged back in successfully, it is strongly recommended to change your password immediately through the application's **Settings** menu).*

> [!QUESTION] User
> Do I lose my account settings with option 1?

> [!NOTE] Gemini
> **No, you will not lose your main data, chat history, or environment configurations**, but you will lose user-specific authentication state.
> 
> Here is exactly what happens when you remove `data/auth.json`:
> 
> ### What is preserved
> 
> -   **Chats & Workspaces:** All saved conversations, agent runs, memories, and workspace files remain intact (these are stored in the SQLite database / vector storage within the `data/` folder).
>     
> -   **System & Model Configurations:** API keys and model parameters defined in your `.env` or system configuration files are untouched.
>     
> 
> ### What is reset
> 
> -   **Admin credentials:** The admin password is replaced by the newly generated temporary password.
>     
> -   **Active sessions:** All currently logged-in browser sessions will be invalidated, requiring a fresh login.
>     
> -   **Additional local accounts:** If you created multiple user accounts inside the UI, their credentials stored inside `auth.json` will be wiped, returning authentication to the default initial state.
>     
> 
> ### Safe Alternative: Rename instead of deleting
> 
> To avoid any permanent loss or accidental corruption, **move (rename)** the file rather than deleting it. That way, you have an immediate fallback:
> 
> Bash
> 
> ```
> docker compose down
> mv data/auth.json data/auth.json.bak
> docker compose up -d --build
> docker compose logs odysseus
> ```
> 
> Once you log in with the new temporary password and confirm everything looks good, you can safely remove `data/auth.json.bak`.

> [!QUESTION] User
> How to safely update odysseus?

> [!NOTE] Gemini
> Updating Odysseus safely involves backing up your persistent data, pulling the updated codebase, checking for new environment variables, and rebuilding your containers.
> 
> 1
> 
> Create a Complete Backup
> 
> Critical Prerequisite
> 
> **1.Create a Complete Backup:**Critical Prerequisite.
> 
> Before pulling code or restarting containers, create a copy of your persistent data and environment configuration:
> 
> Bash
> 
> ```
> cp -r data data_backup_$(date +%Y%m%d_%H%M%S)
> cp .env .env.backup
> ```
> 
> **Verification:** Run `ls -ld data_backup_* .env.backup` to confirm the backup folders and files exist.
> 
> 2
> 
> Stop the Running Containers
> 
> Order is critical
> 
> **2.Stop the Running Containers:**Order is critical.
> 
> Shut down running services cleanly to prevent write operations while files are being replaced:
> 
> Bash
> 
> ```
> docker compose down
> ```
> 
> **Verification:** Run `docker ps` and confirm no Odysseus containers are currently listed.
> 
> 3
> 
> Pull the Latest Code
> 
> Git update
> 
> **3.Pull the Latest Code:**Git update.
> 
> Fetch the latest commits from your tracking branch (typically `main` for stable releases or `dev` for active updates):
> 
> Bash
> 
> ```
> git pull origin main
> ```
> 
> *(If you are tracking the development branch, use `git pull origin dev`)*.
> 
> **Verification:** Git should report `Updating <commit>..<commit>` or `Already up to date` with no merge conflicts.
> 
> 4
> 
> Check for New Environment Variables
> 
> Config review
> 
> **4.Check for New Environment Variables:**Config review.
> 
> New releases often add configuration flags, tool permissions, or model settings. Compare your existing `.env` with the repository's `.env.example`:
> 
> Bash
> 
> ```
> diff -u .env .env.example
> ```
> 
> Merge any new required keys or default values into your active `.env`.
> 
> **Verification:** Open `.env` and verify that any new required variables mentioned in the diff or commit notes are present.
> 
> 5
> 
> Rebuild and Start Containers
> 
> Docker build
> 
> **5.Rebuild and Start Containers:**Docker build.
> 
> Rebuild the container image so all updated backend and frontend dependencies are packaged into the new container:
> 
> Bash
> 
> ```
> docker compose up -d --build
> ```
> 
> **Verification:** Run `docker compose ps` and confirm the `odysseus` container status shows `Up` or `healthy`.
> 
> 6
> 
> Verify Logs and Web Interface
> 
> Health check
> 
> **6.Verify Logs and Web Interface:**Health check.
> 
> Check the container startup logs to ensure database migrations and service initializations completed without exceptions:
> 
> Bash
> 
> ```
> docker compose logs -f odysseus
> ```
> 
> **Verification:** Check the terminal output for clean startup messages and open `http://localhost:7000` in your browser to confirm the UI loads properly with your existing workspaces and chats intact.
> 
> Where would you like to go from here?
> 
> Configure GPU acceleration in Docker Compose
> 
> Roll back to a previous Odysseus version