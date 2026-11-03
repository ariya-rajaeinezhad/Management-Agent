import { useLanguage } from '../contexts/LanguageContext.jsx';
import { t } from '../i18n/translations.js';

export default function LoadingState() {
    const { language } = useLanguage();

    const steps = [
        t('loading_step1', language),
        t('loading_step2', language),
        t('loading_step3', language),
    ];

    return (
        <div className="glass-strong rounded-2xl p-10 border-cyan-500/20 text-center fade-in-up">
            <div className="inline-block mb-6 relative">
                <div className="w-20 h-20 border-4 border-ocean-700 border-t-cyan-400 rounded-full animate-spin"></div>
                <div className="absolute inset-0 w-20 h-20 border-4 border-transparent border-b-gold-500 rounded-full animate-spin" style={{ animationDirection: 'reverse', animationDuration: '2s' }}></div>
            </div>
            <h2 className="text-xl font-bold text-ice-100 mb-4">
                {t('loading_title', language)}
            </h2>
            <div className="space-y-2 max-w-md mx-auto">
                {steps.map((step, i) => (
                    <div key={i} className="flex items-center gap-3 text-ice-200 text-sm">
                        <span className="w-2 h-2 bg-cyan-400 rounded-full animate-pulse"></span>
                        <span>{step}</span>
                    </div>
                ))}
            </div>
            <p className="text-xs text-ice-300/50 mt-6">
                {t('loading_note', language)}
            </p>
        </div>
    );
}