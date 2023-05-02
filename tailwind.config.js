/** @type {import('tailwindcss').Config} */
function generateGridColumns(lastValue) {
  let obj = {}
  for (let i = 1; i < lastValue; i++) {
    obj[`${i}`] = `repeat(${i}, minmax(0, 1fr))`
  }
  return obj
}

module.exports = {
  mode: "jit",
  content: [
    "./src/**/*.html",
    "./src/**/*.js",
  ],
  safelist: [
    'border-amber-300',
    'dark:border-amber-700',
    'border-blue-500',
    'dark:border-teal-600',
    'border-fuchsia-600',
    'dark:border-fuchsia-800',
    'border-gray-200',
    'dark:border-gray-700',
    'shadow-inner',
    'shadow-lg',
    'shadow-sm',
    'shadow-fuchsia-800',
    'shadow-teal-600',
    '-translate-y-1/2',
    'translate',
  ],
  theme: {
    extend: {
      display: ["group-hover"],
      gridTemplateColumns: {
        ...generateGridColumns(6)
      },
    },
  },
  plugins: [
    require('@tailwindcss/line-clamp'),
  ],
}