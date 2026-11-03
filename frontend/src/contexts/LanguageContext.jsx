import { createContext, useContext, useState, useEffect } from 'react';

const LanguageContext = createContext();

export function LanguageProvider({ children }) {
    const [language, setLanguage] = useState(() => {
        // Load from localStorage or default to 'fa'
        return localStorage.getItem('app_language') || 'fa';
    });

    useEffect(() => {
        localStorage.setItem('app_language', language);
        // Update HTML lang attribute
        document.documentElement.lang = language;
        document.documentElement.dir = language === 'fa' ? 'rtl' : 'ltr';
    }, [language]);

    const toggleLanguage = () => {
        setLanguage(prev => prev === 'fa' ? 'en' : 'fa');
    };

    return (
        <LanguageContext.Provider value={{ language, toggleLanguage, isRTL: language === 'fa' }}>
            {children}
        </LanguageContext.Provider>
    );
}

export const useLanguage = () => {
    const context = useContext(LanguageContext);
    if (!context) throw new Error('useLanguage must be used within LanguageProvider');
    return context;
};