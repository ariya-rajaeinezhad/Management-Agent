import { useState, useEffect } from 'react';
import { useLanguage } from './contexts/LanguageContext.jsx';
import { t } from './i18n/translations.js';
import TopicInput from './components/TopicInput.jsx';
import ReportView from './components/ReportView.jsx';
import EnglishAnalysis from './components/EnglishAnalysis.jsx';
import LoadingState from './components/LoadingState.jsx';
import ReportsHistory from './components/ReportsHistory.jsx';
import LanguageSwitcher from './components/LanguageSwitcher.jsx';
import { generateReport, getAllReports } from './services/api.js';

export default function App() {
    const { language } = useLanguage();
    const [activeTab, setActiveTab] = useState('new');
    const [reportData, setReportData] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [showEnglish, setShowEnglish] = useState(false);
    const [history, setHistory] = useState([]);

    const loadHistory = async () => {
        try {
            const data = await getAllReports();
            setHistory(data);
        } catch (err) {
            console.error('Failed to load history:', err);
        }
    };

    useEffect(() => {
        loadHistory();
    }, []);

    const handleSubmit = async (topic) => {
        setLoading(true);
        setError(null);
        setReportData(null);

        try {
            const data = await generateReport(topic, language);
            setReportData(data);
            loadHistory();
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    const handleReset = () => {
        setReportData(null);
        setError(null);
    };

    const handleViewReport = (report) => {
        setReportData({
            final_report: report.final_report,
            topic_en: report.topic_en,
            analysis_en: report.analysis_en,
            report_id: report.id,
        });
        setActiveTab('new');
    };

    return (
        <div className="min-h-screen py-8 px-4">
            <LanguageSwitcher />
            <div className="max-w-5xl mx-auto">
                {/* Header */}
                <header className="text-center mb-8">
                    <div className="inline-flex items-center justify-center w-20 h-20 rounded-2xl glass-strong mb-4 shadow-2xl">
                        <div className="text-4xl">🤖</div>
                    </div>
                    <h1 className="text-5xl font-extrabold mb-2">
                        <span className="gold-text">{t('title', language)}</span>
                    </h1>
                    <p className="text-ice-200 text-lg opacity-80">
                        {t('subtitle', language)}
                    </p>
                </header>

                {/* Tabs */}
                <div className="flex justify-center gap-3 mb-8">
                    <button
                        onClick={() => setActiveTab('new')}
                        className={`tab-btn ${activeTab === 'new' ? 'active' : ''}`}
                    >
                        {t('tab_new', language)}
                    </button>
                    <button
                        onClick={() => { setActiveTab('history'); loadHistory(); }}
                        className={`tab-btn ${activeTab === 'history' ? 'active' : ''}`}
                    >
                        {t('tab_history', language)} ({history.length})
                    </button>
                </div>

                {/* Content */}
                {activeTab === 'history' && !reportData && (
                    <ReportsHistory reports={history} onView={handleViewReport} onRefresh={loadHistory} />
                )}

                {activeTab === 'new' && !reportData && !loading && (
                    <TopicInput onSubmit={handleSubmit} error={error} />
                )}

                {loading && <LoadingState />}

                {reportData && (
                    <div className="space-y-6 fade-in-up">
                        <div className="flex justify-between items-center flex-wrap gap-3">
                            <button
                                onClick={handleReset}
                                className="px-5 py-2 glass rounded-lg text-ice-100 hover:bg-cyan-500/10 transition font-medium border border-cyan-500/30"
                            >
                                {t('new_topic', language)}
                            </button>
                            <label className="flex items-center gap-2 text-ice-200 cursor-pointer select-none">
                                <input
                                    type="checkbox"
                                    checked={showEnglish}
                                    onChange={(e) => setShowEnglish(e.target.checked)}
                                    className="w-4 h-4 accent-cyan-500"
                                />
                                <span className="text-sm">{t('show_english', language)}</span>
                            </label>
                        </div>

                        {showEnglish && (
                            <EnglishAnalysis
                                topicEn={reportData.topic_en}
                                analysisEn={reportData.analysis_en}
                            />
                        )}

                        <ReportView report={reportData.final_report} reportId={reportData.report_id} />
                    </div>
                )}

                <footer className="text-center mt-12 text-ice-300/50 text-sm">
                    {t('footer', language)} — ۲۰۲۶
                </footer>
            </div>
        </div>
    );
}