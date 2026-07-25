# Lightcord - Team Working Rules & Best Practices

## 1. Git Hygiene & Branch Strategy

- **Never commit directly to `main`:** `main` must always contain stable, runnable code.
- **Branch naming convention:** Use prefixes for all new branches:
  - `feature/feature-name` (e.g., `feature/message-input`)
  - `fix/bug-description` (e.g., `fix/websocket-reconnect`)
  - `refactor/scope` (e.g., `refactor/auth-context`)
- **Mandatory Pull Requests:** Every PR requires at least one review and approval from the other partner before merging.
- **Commit Messages:** Keep commits small and use conventional commit formats (e.g., `feat: add chat auto-scroll`, `fix: correct user payload schema`).

## 2. Division of Labor & Workflow

- **Task Management:** Every active task must live on the project board (To Do, In Progress, Done) and be assigned to one person.
- **Define Contracts First:** Before building features that span frontend and backend, document the data structure, API routes, and WebSocket payloads in advance.
- **The 30-Minute Stuck Rule:** If either partner is blocked on a problem or bug for more than 30 minutes, raise it with the other person to pair-program.

## 3. Code Quality & Standards

- **Linter & Formatter:** ESLint and Prettier must be enabled with "Format on Save". Unformatted code should not be pushed.
- **Environment Variables:** Never commit secrets, API keys, or database credentials. Store templates in `.env.example` and list real keys in `.env` (ignored by Git).
- **Directory Consistency:** Stick to the designated file structure. Do not create top-level directories without discussing it first.

## 4. Lightcord Architecture Rules

- **Decouple UI and Real-Time Logic:** Separate WebSocket/Socket.io event listeners and connection logic from UI components using dedicated services or custom hooks.
- **Consistent Error Handling:** Use standard user-facing notifications (e.g., toasts) for runtime errors and enforce consistent API error response schemas.
