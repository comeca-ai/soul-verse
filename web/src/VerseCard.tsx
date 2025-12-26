import React, { useState } from 'react';

interface VerseCardProps {
    reference: string;
    text: string;
    book: string;
    chapter: string;
    verse: string;
}

export const VerseCard: React.FC<VerseCardProps> = ({ reference, text, book, chapter, verse }) => {
    const [copied, setCopied] = useState(false);

    const handleCopy = () => {
        navigator.clipboard.writeText(`${text} (${reference})`);
        setCopied(true);
        setTimeout(() => setCopied(false), 2000);
    };

    return (
        <div className="max-w-md mx-auto my-4 p-8 bg-white rounded-xl shadow-lg border border-gray-100 fade-in relative overflow-hidden">
            {/* Detalhe decorativo no topo */}
            <div className="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-indigo-300 via-purple-300 to-indigo-300 opacity-50"></div>

            {/* Ícone sutil de aspas */}
            <div className="absolute top-6 left-6 text-gray-100 font-serif text-6xl leading-none select-none opacity-50">
                “
            </div>

            <div className="relative z-10 text-center">
                {/* Texto Bíblico */}
                <p className="font-serif text-xl sm:text-2xl text-gray-800 leading-relaxed mb-6 italic">
                    {text}
                </p>

                {/* Referência */}
                <div className="flex flex-col items-center">
                    <span className="text-xs uppercase tracking-widest text-gray-500 font-semibold mb-1">
                        {book} {chapter}:{verse}
                    </span>
                    <div className="h-px w-12 bg-indigo-200 my-2"></div>
                </div>

                {/* Ações */}
                <div className="mt-6 flex justify-center">
                    <button
                        onClick={handleCopy}
                        className={`
              flex items-center gap-2 px-4 py-2 rounded-full text-sm font-medium transition-all duration-300
              ${copied
                                ? 'bg-green-50 text-green-700 ring-1 ring-green-200'
                                : 'bg-gray-50 text-gray-600 hover:bg-indigo-50 hover:text-indigo-600'}
            `}
                        aria-label="Copiar versículo"
                    >
                        {copied ? (
                            <>
                                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M5 13l4 4L19 7" /></svg>
                                <span>Copiado</span>
                            </>
                        ) : (
                            <>
                                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" /></svg>
                                <span>Copiar</span>
                            </>
                        )}
                    </button>
                </div>
            </div>
        </div>
    );
};
