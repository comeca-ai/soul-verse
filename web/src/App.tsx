import { useEffect, useState } from 'react';
import { VerseCard } from './VerseCard';

type VersePayload = {
  kind: 'verse_card';
  theme: string;
  feeling: string;
  display: {
    heading: string;
    subheading: string;
    book: string;
    chapter: string;
    verse: string;
    full_text: string;
    reference: string;
    translation?: string;
    theme_color?: string;
  };
  reflection: string;
  suggested_follow_up?: string;
  limitations?: string[];
};

type ErrorPayload = {
  kind: 'error_card';
  title: string;
  message: string;
  suggestion?: string;
};

type SoulVersePayload = VersePayload | ErrorPayload;

declare global {
  interface Window {
    openai?: {
      toolOutput?: unknown;
      toolResult?: unknown;
    };
  }
}

const MOCK_DATA: VersePayload = {
  kind: 'verse_card',
  theme: 'ansiedade',
  feeling: 'estou ansioso com o trabalho',
  display: {
    heading: 'Respire e entregue isso a Deus',
    subheading: 'Verso para ansiedade e excesso de preocupacao.',
    book: 'Filipenses',
    chapter: '4',
    verse: '6-7',
    full_text:
      'Nao andeis ansiosos por coisa alguma; antes, em tudo, sejam os vossos pedidos conhecidos diante de Deus pela oracao e pela suplica, com acoes de gracas.',
    reference: 'Filipenses 4:6-7',
    translation: 'almeida',
    theme_color: '#7c3aed',
  },
  reflection:
    'Este versiculo lembra que a ansiedade pode ser levada a Deus em oracao, com honestidade e calma.',
  suggested_follow_up:
    'Se quiser, eu posso trazer outro versiculo mais focado em paz e descanso.',
  limitations: [
    'O texto do versiculo vem de uma API biblica publica.',
    'O app nao substitui cuidado pastoral, psicologico ou medico.',
  ],
};

function coercePayload(value: unknown): SoulVersePayload | null {
  if (!value || typeof value !== 'object') {
    return null;
  }

  const candidate = value as Record<string, unknown>;

  if (candidate.structuredContent && typeof candidate.structuredContent === 'object') {
    return coercePayload(candidate.structuredContent);
  }

  if (candidate.kind === 'verse_card' || candidate.kind === 'error_card') {
    return candidate as SoulVersePayload;
  }

  return null;
}

function readToolPayload(): SoulVersePayload | null {
  const fromToolOutput = coercePayload(window.openai?.toolOutput);
  if (fromToolOutput) {
    return fromToolOutput;
  }

  const fromToolResult = coercePayload(window.openai?.toolResult);
  if (fromToolResult) {
    return fromToolResult;
  }

  return null;
}

function App() {
  const [data, setData] = useState<SoulVersePayload | null>(null);

  useEffect(() => {
    const payload = readToolPayload();

    if (payload) {
      setData(payload);
      return;
    }

    const timer = setTimeout(() => {
      setData(MOCK_DATA);
    }, 250);

    return () => clearTimeout(timer);
  }, []);

  return (
    <div className="min-h-screen bg-[radial-gradient(circle_at_top,_#fbf7ff_0%,_#f5f7fb_48%,_#eef2ff_100%)] p-4 text-slate-900">
      <div className="mx-auto flex min-h-screen w-full max-w-2xl items-center justify-center">
        {!data ? (
          <div className="w-full animate-pulse rounded-[28px] border border-white/60 bg-white/75 p-8 shadow-[0_18px_70px_rgba(76,29,149,0.12)] backdrop-blur">
            <div className="mb-6 h-8 w-2/3 rounded-full bg-slate-200" />
            <div className="mb-3 h-4 w-full rounded-full bg-slate-200" />
            <div className="mb-3 h-4 w-5/6 rounded-full bg-slate-200" />
            <div className="h-40 rounded-[22px] bg-slate-100" />
          </div>
        ) : data.kind === 'error_card' ? (
          <div className="w-full rounded-[28px] border border-rose-200 bg-white/90 p-8 shadow-[0_18px_70px_rgba(15,23,42,0.12)] backdrop-blur">
            <p className="mb-2 text-xs font-semibold uppercase tracking-[0.28em] text-rose-500">
              SoulVerse
            </p>
            <h1 className="mb-3 text-3xl font-semibold text-slate-900">{data.title}</h1>
            <p className="mb-4 text-base leading-7 text-slate-600">{data.message}</p>
            {data.suggestion ? (
              <p className="rounded-2xl bg-rose-50 px-4 py-3 text-sm text-rose-700">
                {data.suggestion}
              </p>
            ) : null}
          </div>
        ) : (
          <VerseCard
            heading={data.display.heading}
            subheading={data.display.subheading}
            reference={data.display.reference}
            text={data.display.full_text}
            book={data.display.book}
            chapter={data.display.chapter}
            verse={data.display.verse}
            themeColor={data.display.theme_color}
            reflection={data.reflection}
            followUp={data.suggested_follow_up}
            feeling={data.feeling}
            translation={data.display.translation}
          />
        )}
      </div>
    </div>
  );
}

export default App;
