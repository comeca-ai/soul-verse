import { useState } from 'react';

interface VerseCardProps {
  heading: string;
  subheading: string;
  reference: string;
  text: string;
  book: string;
  chapter: string;
  verse: string;
  themeColor?: string;
  reflection: string;
  followUp?: string;
  feeling: string;
  translation?: string;
}

export function VerseCard({
  heading,
  subheading,
  reference,
  text,
  book,
  chapter,
  verse,
  themeColor = '#7c3aed',
  reflection,
  followUp,
  feeling,
  translation,
}: VerseCardProps) {
  const [copied, setCopied] = useState(false);

  async function handleCopy() {
    try {
      await navigator.clipboard.writeText(`${text} (${reference})`);
      setCopied(true);
      window.setTimeout(() => setCopied(false), 1800);
    } catch {
      setCopied(false);
    }
  }

  return (
    <article className="w-full overflow-hidden rounded-[30px] border border-white/70 bg-white/88 shadow-[0_24px_90px_rgba(76,29,149,0.12)] backdrop-blur">
      <div
        className="relative overflow-hidden px-7 pb-7 pt-8 text-white"
        style={{
          background: `linear-gradient(135deg, ${themeColor} 0%, #1d4ed8 100%)`,
        }}
      >
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_top_right,_rgba(255,255,255,0.24),_transparent_36%)]" />
        <div className="relative">
          <p className="mb-3 text-[11px] font-semibold uppercase tracking-[0.32em] text-white/80">
            SoulVerse
          </p>
          <h1 className="max-w-xl text-3xl font-semibold leading-tight sm:text-[2.35rem]">
            {heading}
          </h1>
          <p className="mt-3 max-w-2xl text-sm leading-6 text-white/86 sm:text-base">
            {subheading}
          </p>
        </div>
      </div>

      <div className="space-y-6 px-7 py-7">
        <section className="grid gap-3 rounded-[24px] border border-slate-200 bg-slate-50/80 p-5 sm:grid-cols-3">
          <div>
            <p className="mb-1 text-[11px] font-semibold uppercase tracking-[0.24em] text-slate-500">
              Sentimento
            </p>
            <p className="text-sm font-medium text-slate-900">{feeling}</p>
          </div>
          <div>
            <p className="mb-1 text-[11px] font-semibold uppercase tracking-[0.24em] text-slate-500">
              Referencia
            </p>
            <p className="text-sm font-medium text-slate-900">{reference}</p>
          </div>
          <div>
            <p className="mb-1 text-[11px] font-semibold uppercase tracking-[0.24em] text-slate-500">
              Traducao
            </p>
            <p className="text-sm font-medium text-slate-900">
              {(translation || 'almeida').toUpperCase()}
            </p>
          </div>
        </section>

        <section className="relative overflow-hidden rounded-[28px] border border-slate-200 bg-white p-7 shadow-[0_10px_30px_rgba(15,23,42,0.05)]">
          <div className="absolute left-6 top-4 text-7xl leading-none text-slate-100">“</div>
          <div className="relative">
            <p className="font-serif text-[1.35rem] leading-9 text-slate-800 sm:text-[1.55rem]">
              {text}
            </p>
            <div className="mt-6 flex flex-wrap items-center gap-3">
              <span className="inline-flex items-center rounded-full bg-slate-100 px-3 py-1 text-xs font-semibold uppercase tracking-[0.2em] text-slate-600">
                {book} {chapter}:{verse}
              </span>
              <button
                type="button"
                onClick={handleCopy}
                className={`rounded-full px-4 py-2 text-sm font-medium transition ${
                  copied
                    ? 'bg-emerald-50 text-emerald-700 ring-1 ring-emerald-200'
                    : 'bg-slate-900 text-white hover:bg-slate-800'
                }`}
              >
                {copied ? 'Copiado' : 'Copiar versiculo'}
              </button>
            </div>
          </div>
        </section>

        <section className="grid gap-4 sm:grid-cols-[1.2fr_0.8fr]">
          <div className="rounded-[24px] border border-slate-200 bg-white p-5">
            <p className="mb-2 text-[11px] font-semibold uppercase tracking-[0.28em] text-slate-500">
              Reflexao
            </p>
            <p className="text-sm leading-7 text-slate-700">{reflection}</p>
          </div>
          <div className="rounded-[24px] border border-slate-200 bg-slate-50/80 p-5">
            <p className="mb-2 text-[11px] font-semibold uppercase tracking-[0.28em] text-slate-500">
              Continuacao
            </p>
            <p className="text-sm leading-7 text-slate-700">
              {followUp || 'Posso trazer outro versiculo relacionado, se quiser.'}
            </p>
          </div>
        </section>
      </div>
    </article>
  );
}
