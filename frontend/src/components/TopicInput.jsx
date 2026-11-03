import { useState } from 'react';
import { useLanguage } from '../contexts/LanguageContext.jsx';
import { t } from '../i18n/translations.js';

export default function TopicInput({ onSubmit, error }) {
    const { language } = useLanguage();
    const [topic, setTopic] = useState('');

    const examples = [t('example1', language), t('example2', language), t('example3', language)];

    const handleSubmit = (e) => {
        e.preventDefault();
        if (topic.trim().length >= 5) {
            onSubmit(topic.trim());
        }
    };

    return (
        <div className="glass-strong rounded-2xl p-8 shadow-2xl fade-in-up">
            <form onSubmit={handleSubmit}>
                <label className="block text-ice-100 font-semibold mb-3 text-lg">
                    {t('input_label', language)}
                </label>
                <textarea
                    value={topic}
                    onChange={(e) => setTopic(e.target.value)}
                    placeholder={t('input_placeholder', language)}
                    rows={4}
                    maxLength={2000}
                    className="w-full px-4 py-3 bg-ocean-900/60 border-2 border-cyan-500/20 rounded-xl focus:border-cyan-400 focus:outline-none transition resize-none text-ice-100 placeholder:text-ice-300/40"
                />
                <div className="flex justify-between items-center mt-2 mb-4">
                    <span className="text-xs text-ice-300/50">
                        {topic.length} / 2000 {t('char_count', language)}
                    </span>
                </div>

                {error && (
                    <div className="mb-4 p-3 bg-red-500/10 border border-red-400/30 text-red-300 rounded-lg text-sm">
                        ⚠️ {error}
                    </div>
                )}

                <button
                    type="submit"
                    disabled={topic.trim().length < 5}
                    className="w-full py-3 bg-gradient-to-l from-cyan-500 to-ocean-600 text-white font-bold rounded-xl shadow-lg hover:shadow-cyan-500/30 disabled:opacity-50 disabled:cursor-not-allowed transition border border-cyan-400/30"
                >
                    {t('generate_btn', language)}
                </button>
            </form>

            <div className="mt-6 pt-6 border-t border-cyan-500/10">
                <p className="text-sm text-ice-300/70 mb-3">{t('examples', language)}</p>
                <div className="flex flex-wrap gap-2">
                    {examples.map((ex, i) => (
                        <button
                            key={i}
                            onClick={() => setTopic(ex)}
                            className="text-xs px-3 py-1.5 bg-ocean-800/50 hover:bg-cyan-500/10 text-ice-200 rounded-full transition border border-cyan-500/10 hover:border-cyan-400/30"
                        >
                            {ex}
                        </button>
                    ))}
                </div>
            </div>
        </div>
    );
}