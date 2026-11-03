export default function EnglishAnalysis({ topicEn, analysisEn }) {
    return (
        <div className="glass rounded-xl p-6 border-ocean-600/40 fade-in-up">
            <h3 className="text-lg font-bold text-ice-100 mb-3 flex items-center gap-2">
                <span>🇬🇧</span> English Internal Analysis
            </h3>
            <div className="space-y-3">
                <div>
                    <span className="text-xs font-semibold text-cyan-400 uppercase">
                        Translated Topic
                    </span>
                    <p className="text-ice-200 mt-1 bg-ocean-900/60 p-3 rounded-lg border border-cyan-500/20">
                        {topicEn}
                    </p>
                </div>
                <div>
                    <span className="text-xs font-semibold text-cyan-400 uppercase">
                        Structured Analysis (JSON)
                    </span>
                    <pre className="text-xs text-ice-200 mt-1 bg-ocean-900/60 p-4 rounded-lg border border-cyan-500/20 overflow-x-auto max-h-96 overflow-y-auto" dir="ltr">
                        {JSON.stringify(analysisEn, null, 2)}
                    </pre>
                </div>
            </div>
        </div>
    );
}