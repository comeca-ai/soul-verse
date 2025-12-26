/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {
            fontFamily: {
                sans: ['Inter', 'sans-serif'],
                serif: ['Merriweather', 'serif'], // Para o texto bíblico ficar elegante
            },
            colors: {
                'soul-primary': '#4F46E5', // Indigo
                'soul-bg': '#F3F4F6',
                'soul-card': '#FFFFFF',
            }
        },
    },
    plugins: [],
}
