# 🤖 AI Management Agent - Frontend

A modern, bilingual (Persian/English) React frontend with an ocean-themed UI for the AI Management Agent.

## 🎨 Features

- 🌐 **Full Bilingual Support (i18n)**: Seamless switching between Persian (RTL) and English (LTR)
- 🎨 **Ocean Dark Theme**: Premium glassmorphism design with cyan and gold accents
- 📱 **Fully Responsive**: Optimized for mobile, tablet, and desktop
- 📚 **Report Archive**: View, edit, and delete saved reports
- 📥 **Markdown Export**: Download reports as `.md` files
- ⚡ **Fast Performance**: Built with Vite for instant hot-reload

## 🛠️ Tech Stack

- **React 18** - UI library
- **Vite 5** - Build tool
- **Tailwind CSS v4** - Styling framework
- **React Markdown** - Content rendering
- **Vazirmatn** - Persian/Arabic font

## 📁 Project Structure

```text
frontend/
├── src/
│   ├── components/         # React components
│   │   ├── EnglishAnalysis.jsx
│   │   ├── LanguageSwitcher.jsx
│   │   ├── LoadingState.jsx
│   │   ├── ReportSection.jsx
│   │   ├── ReportsHistory.jsx
│   │   ├── ReportView.jsx
│   │   └── TopicInput.jsx
│   ├── contexts/           # React contexts
│   │   └── LanguageContext.jsx
│   ├── i18n/               # Translations
│   │   └── translations.js
│   ├── services/           # API client
│   │   └── api.js
│   ├── App.jsx             # Main application
│   ├── index.css           # Global styles (Ocean theme)
│   └── main.jsx            # Entry point
├── index.html
├── package.json
└── vite.config.js
```

## 🚀 Local Setup

### 1. Install Dependencies

```bash
npm install
```

### 2. Configure Environment

Create a `.env` file in the root directory:

```env
VITE_API_URL=http://127.0.0.1:8000/api
```

> **Important**: Make sure the backend is running on port 8000 before starting the frontend.

### 3. Run Development Server

```bash
npm run dev
```

The app will be available at `http://localhost:5173`

### 4. Build for Production

```bash
npm run build
```

Output will be in the `dist/` directory.

## 🎨 Design System

### Color Palette

- **Ocean Dark**: `#0a1929` - Deep navy background
- **Cyan**: `#22d3ee` - Primary accent
- **Gold**: `#d4af37` - Titles and highlights
- **Ice**: `#e0f2fe` - Text color

### Typography

- **Font**: Vazirmatn (supports Persian, Arabic, and English)
- **RTL Support**: Full right-to-left layout for Persian

### Effects

- **Glassmorphism**: Frosted glass cards with backdrop blur
- **Gold Shimmer**: Animated gradient on titles
- **Fade-in-up**: Smooth entry animations

## ☁️ Deployment

### Vercel (Recommended)

1. Push your code to GitHub
2. Import the project in Vercel
3. Set environment variable:
   - `VITE_API_URL` = your backend URL (e.g., `https://your-backend.vercel.app/api`)
4. Deploy!

### Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `VITE_API_URL` | Backend API base URL | `http://127.0.0.1:8000/api` |

## 🔌 Backend Connection

This frontend communicates with the FastAPI backend. Make sure:
- Backend is running on the configured `VITE_API_URL`
- CORS is properly configured on the backend to allow your frontend's origin

## 📄 License

Academic project - created for educational purposes.
