# community-health-pwa: Offline-First Progressive Web App for Health Extension Workers

A mobile-first, bilingual (Amharic & English) Progressive Web App engineered for Health Extension Workers (HEWs) and mobile health teams in remote pastoralist communities across Afar and East Africa.

## Features
- **Offline First**: ServiceWorker caching and IndexedDB local queuing for continuous data capture without mobile network coverage.
- **Background Synchronization**: Automatically posts queued maternal and child screening records to the clinic server upon network restoration.
- **FastAPI Core**: Microservice endpoint handling batch intake synchronization.
