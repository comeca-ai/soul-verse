import { useEffect, useState } from 'react';
import { VerseCard } from './VerseCard';

// Tipagem do payload esperado do 'backend'
interface VersePayload {
  kind: 'verse_card';
  display: {
    book: string;
    chapter: string;
    verse: string;
    full_text: string;
    theme_color?: string;
    reference: string;
  };
}

// Mock inicial para visualização em desenvolvimento (quando não tem backend real conectado)
const MOCK_DATA: VersePayload = {
  kind: 'verse_card',
  display: {
    book: "Salmos",
    chapter: "23",
    verse: "1",
    full_text: "O SENHOR é o meu pastor, nada me faltará.",
    reference: "Salmos 23:1"
  }
};

function App() {
  const [data, setData] = useState<VersePayload | null>(null);

  useEffect(() => {
    // Em produção, leríamos window.openai.toolOutput ou similar.
    // Aqui, para demo, carregamos o mock após um breve delay para simular 'chegada'
    const timer = setTimeout(() => {
      setData(MOCK_DATA);
    }, 500);
    return () => clearTimeout(timer);
  }, []);

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50 p-4">
      <div className="w-full max-w-lg">
        {!data ? (
          <div className="flex flex-col items-center justify-center space-y-4 animate-pulse">
            <div className="h-40 w-full bg-gray-200 rounded-xl"></div>
            <p className="text-gray-400 text-sm">Buscando inspiração...</p>
          </div>
        ) : (
          <VerseCard
            reference={data.display.reference}
            text={data.display.full_text}
            book={data.display.book}
            chapter={data.display.chapter}
            verse={data.display.verse}
          />
        )}

        <div className="mt-8 text-center">
          <p className="text-xs text-gray-400">
            SoulVerse Widget • Powered by Bible API
          </p>
        </div>
      </div>
    </div>
  );
}

export default App;
