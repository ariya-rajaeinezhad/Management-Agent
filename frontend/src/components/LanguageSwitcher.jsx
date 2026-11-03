import { useLanguage } from '../contexts/LanguageContext';

export default function LanguageSwitcher() {
    const { language, toggleLanguage } = useLanguage();

    return (
        <button
            onClick={toggleLanguage}
            className="fixed top-4 left-4 z-50 glass-strong px-4 py-2 rounded-full flex items-center gap-2 hover:scale-105 transition-transform border border-cyan-400/30"
            title={language === 'fa' ? 'Switch to English' : 'تغییر به فارسی'}
        >
            <span className="text-md font-bold">{language === 'fa' ? 'EN' : 'fa'}</span>
        </button>
    );
}