# Community Health PWA

A mobile-first, bilingual Progressive Web App designed for Health Extension Workers and community health teams operating in remote and low-connectivity environments.

## Project Overview

This project is built to support frontline health workers in areas with limited mobile internet access. It enables offline health data capture, patient screening, and timely synchronization when connectivity is restored.

## Key Features

- Offline-first data capture with local storage
- Service worker-based caching and reliability
- IndexedDB queueing for delayed upload
- Background synchronization after connectivity is restored
- Bilingual interface in Amharic and English
- Designed for maternal and child health workflows
- Mobile-first UX for field health workers

## Why This Project Matters

Health extension workers often operate in rural and mobile environments where network coverage is inconsistent. This application helps them continue collecting important patient data without interrupting routine workflows.

## Core Use Cases

- Maternal and child health screening
- Community-based risk assessment
- Referral tracking and follow-up records
- Remote health worker data capture
- Offline-first reporting in underserved locations

## Tech Stack

- Progressive Web App (PWA)
- Service worker and offline caching
- IndexedDB or local persistence layer
- FastAPI backend services for synchronization
- Mobile-first responsive frontend

## Installation

### Frontend

```bash
git clone https://github.com/Hailegiorgisy/community_health_pwa.git
cd community_health_pwa
npm install
npm run dev
```

### Backend (if applicable)

```bash
pip install -r requirements.txt
python app.py
```

## Workflow

1. Health worker opens the PWA on a mobile device
2. Records community health data while offline
3. Data is stored locally in the browser storage layer
4. When internet connectivity returns, queued submissions sync automatically
5. Server receives structured records for follow-up and reporting

## Example User Experience

- Enter patient or household details
- Capture screening questions
- Save data locally when offline
- Review pending uploads
- Sync automatically when the network is available

## Repository Structure

```text
community_health_pwa/
├── frontend/
├── backend/
├── public/
├── src/
├── data/
├── README.md
├── package.json
├── requirements.txt
└── .env.example
```

## Offline-first Design Principles

- Data must be resilient to dropped connectivity
- Forms should remain useful without real-time network access
- Uploads should be retried automatically
- User actions should be lightweight and accessible on low-end devices

## Contributing

Contributions are welcome, especially in improving usability for community health teams, reducing data entry friction, and extending offline workflows.

## License

This project is open-source and distributed under the MIT license unless otherwise specified in the repository.
