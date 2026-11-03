import { useState } from 'react';
import { getReport, deleteReport } from '../services/api.js';
import { useLanguage } from '../contexts/LanguageContext.jsx';
import { t } from '../i18n/translations.js';

export default function ReportsHistory({ reports, onView, onRefresh }) {
    const { language } = useLanguage();
    const [deletingId, setDeletingId] = useState(null);
    const [confirmDelete, setConfirmDelete] = useState(null);

    const handleDelete = async (id) => {
        setDeletingId(id);
        try {
            await deleteReport(id);
            onRefresh();
        } catch (err) {
            alert(language === 'fa' ? 'خطا در حذف گزارش' : 'Failed to delete report');
        } finally {
            setDeletingId(null);
            setConfirmDelete(null);
        }
    };

    const handleView = async (id) => {
        try {
            const report = await getReport(id);
            onView(report);
        } catch (err) {
            alert(language === 'fa' ? 'خطا در بارگذاری گزارش' : 'Failed to load report');
        }
    };

    const formatDate = (isoString) => {
        try {
            const date = new Date(isoString);
            if (language === 'fa') {
                return date.toLocaleString('fa-IR', {
                    year: 'numeric',
                    month: 'short',
                    day: 'numeric',
                    hour: '2-digit',
                    minute: '2-digit',
                });
            } else {
                return date.toLocaleString('en-US', {
                    year: 'numeric',
                    month: 'short',
                    day: 'numeric',
                    hour: '2-digit',
                    minute: '2-digit',
                });
            }
        } catch {
            return isoString;
        }
    };

    if (reports.length === 0) {
        return (
            <div className="glass-strong rounded-2xl p-12 text-center fade-in-up">
                <div className="text-6xl mb-4">📭</div>
                <h3 className="text-xl font-bold text-ice-100 mb-2">{t('history_empty', language)}</h3>
                <p className="text-ice-300/70">{t('history_empty_desc', language)}</p>
            </div>
        );
    }

    return (
        <div className="space-y-3 fade-in-up">
            <div className="glass-strong rounded-2xl p-6">
                <h3 className="text-xl font-bold text-ice-100 mb-4 flex items-center gap-2">
                    <span>📚</span> {t('history_title', language)}
                </h3>
                <div className="space-y-3">
                    {reports.map((report) => (
                        <div
                            key={report.id}
                            className="glass rounded-xl p-4 hover:border-cyan-400/40 transition group"
                        >
                            <div className="flex justify-between items-start gap-3">
                                <div className="flex-1 min-w-0">
                                    <p className="text-ice-100 font-medium line-clamp-2 mb-2">
                                        {report.topic_fa}
                                    </p>
                                    <div className="flex gap-4 text-xs text-ice-300/60">
                                        <span>{t('created', language)}: {formatDate(report.created_at)}</span>
                                        {report.updated_at !== report.created_at && (
                                            <span>{t('updated', language)}: {formatDate(report.updated_at)}</span>
                                        )}
                                    </div>
                                </div>
                                <div className="flex gap-2 opacity-60 group-hover:opacity-100 transition">
                                    <button
                                        onClick={() => handleView(report.id)}
                                        className="px-3 py-1.5 bg-cyan-500/20 hover:bg-cyan-500/30 text-cyan-300 rounded-lg text-sm font-medium transition border border-cyan-500/30"
                                    >
                                        {t('view', language)}
                                    </button>
                                    {confirmDelete === report.id ? (
                                        <div className="flex gap-1">
                                            <button
                                                onClick={() => handleDelete(report.id)}
                                                disabled={deletingId === report.id}
                                                className="px-3 py-1.5 bg-red-500/20 hover:bg-red-500/30 text-red-300 rounded-lg text-sm font-medium transition border border-red-500/30 disabled:opacity-50"
                                            >
                                                {deletingId === report.id ? '...' : t('confirm_delete', language)}
                                            </button>
                                            <button
                                                onClick={() => setConfirmDelete(null)}
                                                className="px-3 py-1.5 bg-ocean-800 hover:bg-ocean-700 text-ice-200 rounded-lg text-sm transition"
                                            >
                                                {t('cancel_delete', language)}
                                            </button>
                                        </div>
                                    ) : (
                                        <button
                                            onClick={() => setConfirmDelete(report.id)}
                                            className="px-3 py-1.5 bg-red-500/10 hover:bg-red-500/20 text-red-300 rounded-lg text-sm transition border border-red-500/20"
                                        >
                                            {t('delete', language)}
                                        </button>
                                    )}
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
}