import { useState } from 'react';

export default function ReportSection({ number, title, icon, children, defaultOpen = false }) {
    const [isOpen, setIsOpen] = useState(defaultOpen);

    return (
        <div className="glass rounded-xl overflow-hidden hover:border-cyan-400/30 transition">
            <button
                onClick={() => setIsOpen(!isOpen)}
                className="w-full flex items-center justify-between p-5 hover:bg-cyan-500/5 transition text-right"
            >
                <div className="flex items-center gap-3">
                    <span className="text-2xl">{icon}</span>
                    <div>
                        <span className="text-xs text-cyan-400 font-semibold block">
                            {number}
                        </span>
                        <h3 className="text-lg font-bold text-ice-100">{title}</h3>
                    </div>
                </div>
                <svg
                    className={`w-5 h-5 text-cyan-400 transition-transform ${isOpen ? 'rotate-180' : ''}`}
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                >
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
                </svg>
            </button>
            {isOpen && (
                <div className="px-6 pb-6 border-t border-cyan-500/10 pt-4">
                    <div className="markdown-content">{children}</div>
                </div>
            )}
        </div>
    );
}