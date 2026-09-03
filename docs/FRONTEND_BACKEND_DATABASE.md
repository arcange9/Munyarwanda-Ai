# Munyarwanda AI — Frontend, Backend & Database

## Current architecture

Munyarwanda AI uses a Next.js application where the UI and server API routes live in the same repository. This keeps development simple while preserving a clean boundary between presentation, API, AI providers, retrieval, and persistence.

### Frontend
- `app/` — pages and API route entry points
- `components/` — reusable UI components
- `app/chat/` — main assistant experience
- `app/explore/` — exploration experience
- `app/translate/` — translation experience
- `app/about/` — project information

### Backend
- `app/api/chat/` — streaming chat endpoint
- `app/api/auth/` — authentication endpoints
- `app/api/conversations/` — authenticated conversation CRUD
- `lib/ai/` — provider abstraction and prompts
- `lib/web-search.ts` — Google web-research bridge
- `lib/rate-limit.ts` — request throttling

### Database
PostgreSQL + Prisma is the persistence layer. The schema covers users, conversations, messages, documents, research runs, research sources, user feedback, and audit logs.

## Target product flow

`User → Next.js UI → API → Auth/Rate limit → Tools/RAG/Web Research → AI Provider → Response → Persistence`

## Future model swap
The AI provider layer is deliberately abstracted. The production path can move from a hosted API to a self-hosted Munyarwanda model without rewriting the chat UI.

## Production rule
Do not commit secrets, raw private datasets, model weights, database dumps, or user documents to GitHub. Keep credentials in deployment environment variables and keep large/restricted datasets outside the source repository.
