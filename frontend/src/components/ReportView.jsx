import { useState } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import { useLanguage } from '../contexts/LanguageContext.jsx';
import { t } from '../i18n/translations.js';
import ReportSection from './ReportSection.jsx';
import { updateReportTitle } from '../services/api.js';

export default function ReportView({ report, reportId }) {
    const { language } = useLanguage();
    const [isEditing, setIsEditing] = useState(false);
    const [editTitle, setEditTitle] = useState(report.project_title);

    const downloadMarkdown = () => {
        const md = buildMarkdown(report, language);
        const blob = new Blob([md], { type: 'text/markdown;charset=utf-8' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `management_report_${language}.md`;
        a.click();
        URL.revokeObjectURL(url);
    };

    const handleSaveTitle = async () => {
        if (!reportId) {
            report.project_title = editTitle;
            setIsEditing(false);
            return;
        }
        try {
            const updated = await updateReportTitle(reportId, editTitle);
            report.project_title = updated.final_report.project_title;
            setIsEditing(false);
        } catch (err) {
            alert(language === 'fa' ? 'خطا در ذخیره عنوان' : 'Error saving title');
        }
    };

    // Section numbers with prefix based on language
    const sectionNumbers = language === 'fa'
        ? ['بخش ۱', 'بخش ۲', 'بخش ۳', 'بخش ۴', 'بخش ۵', 'بخش ۶', 'بخش ۷', 'بخش ۸', 'بخش ۹', 'بخش ۱۰']
        : ['Section 1', 'Section 2', 'Section 3', 'Section 4', 'Section 5', 'Section 6', 'Section 7', 'Section 8', 'Section 9', 'Section 10'];

    // Section labels from translations
    const sectionLabels = [
        t('section1', language),
        t('section2', language),
        t('section3', language),
        t('section4', language),
        t('section5', language),
        t('section6', language),
        t('section7', language),
        t('section8', language),
        t('section9', language),
        t('section10', language)
    ];

    const sectionIcons = ['🎯', '⚠️', '📅', '🏢', '🧭', '📊', '📈', '🛡️', '💡', '🎓'];

    const sectionKeys = [
        'problem_definition',
        'assumptions_and_constraints',
        'planning',
        'organizing',
        'leading',
        'controlling',
        'kpis',
        'risks',
        'final_recommendations',
        'conclusion'
    ];

    return (
        <div className="space-y-4">
            {/* Title Card */}
            <div className="relative overflow-hidden rounded-2xl p-8 shadow-2xl fade-in-up"
                style={{ background: 'linear-gradient(135deg, #0d2847 0%, #143a5f 50%, #1a4d7a 100%)' }}>
                <div className="relative">
                    <span className="text-sm text-cyan-400 opacity-80">{t('report_label', language)}</span>

                    {isEditing ? (
                        <div className="mt-2 flex gap-2">
                            <input
                                type="text"
                                value={editTitle}
                                onChange={(e) => setEditTitle(e.target.value)}
                                className="flex-1 px-4 py-2 bg-ocean-900/60 border-2 border-cyan-400/40 rounded-lg text-ice-100 focus:outline-none"
                                autoFocus
                            />
                            <button onClick={handleSaveTitle} className="px-4 py-2 bg-cyan-500 text-ocean-950 font-bold rounded-lg hover:bg-cyan-400">
                                {t('save', language)}
                            </button>
                            <button onClick={() => { setIsEditing(false); setEditTitle(report.project_title); }} className="px-4 py-2 bg-ocean-800 text-ice-200 rounded-lg">
                                {t('cancel', language)}
                            </button>
                        </div>
                    ) : (
                        <div className="flex items-center gap-3 mt-2">
                            <h2 className="text-3xl font-extrabold text-ice-50">{report.project_title}</h2>
                            {reportId && (
                                <button onClick={() => setIsEditing(true)} className="text-gold-400 hover:text-gold-500" title={t('edit_title', language)}>
                                    ✏️
                                </button>
                            )}
                        </div>
                    )}

                    <button onClick={downloadMarkdown} className="mt-4 px-4 py-2 bg-white/10 hover:bg-white/20 rounded-lg text-sm font-medium transition border border-white/20 text-ice-100">
                        {t('download_md', language)}
                    </button>
                </div>
            </div>

            {/* Executive Summary */}
            <div className="glass rounded-xl p-6">
                <h3 className="text-lg font-bold text-ice-100 mb-3">{t('exec_summary', language)}</h3>
                <div className="markdown-content">
                    <ReactMarkdown remarkPlugins={[remarkGfm]}>{report.executive_summary}</ReactMarkdown>
                </div>
            </div>

            {/* All 10 Sections */}
            {sectionKeys.map((key, i) => {
                const content = report[key];
                const isList = key === 'assumptions_and_constraints';

                return (
                    <ReportSection
                        key={key}
                        number={sectionNumbers[i]}
                        title={sectionLabels[i]}
                        icon={sectionIcons[i]}
                        defaultOpen={i === 2}
                    >
                        {isList ? (
                            <ul className="list-disc space-y-1">
                                {content.map((item, idx) => <li key={idx}>{item}</li>)}
                            </ul>
                        ) : (
                            <ReactMarkdown remarkPlugins={[remarkGfm]}>{content}</ReactMarkdown>
                        )}
                    </ReportSection>
                );
            })}
        </div>
    );
}

function buildMarkdown(report, language) {
    const isFa = language === 'fa';
    const sectionLabels = isFa ? [
        'تعریف مسئله', 'مفروضات و محدودیت‌ها', 'برنامه‌ریزی', 'سازماندهی',
        'هدایت و اجرا', 'کنترل و ارزیابی', 'شاخص‌های کلیدی عملکرد',
        'ریسک‌ها و راهکارهای مقابله', 'پیشنهادات نهایی', 'نتیجه‌گیری'
    ] : [
        'Problem Definition', 'Assumptions & Constraints', 'Planning', 'Organizing',
        'Leading & Execution', 'Controlling & Evaluation', 'Key Performance Indicators',
        'Risks & Mitigation', 'Final Recommendations', 'Conclusion'
    ];

    let md = `# ${report.project_title}\n\n`;
    md += `## ${isFa ? 'خلاصه مدیریتی' : 'Executive Summary'}\n${report.executive_summary}\n\n`;

    const sectionKeys = [
        'problem_definition', 'assumptions_and_constraints', 'planning', 'organizing',
        'leading', 'controlling', 'kpis', 'risks', 'final_recommendations', 'conclusion'
    ];

    sectionKeys.forEach((key, i) => {
        md += `## ${i + 1}. ${sectionLabels[i]}\n`;
        if (key === 'assumptions_and_constraints') {
            report[key].forEach(item => { md += `- ${item}\n`; });
        } else {
            md += `${report[key]}\n`;
        }
        md += '\n';
    });

    return md;
}