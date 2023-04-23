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
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {
      display: ["group-hover"],
      gridTemplateColumns: {
        ...generateGridColumns(6)
      }
    },
  },
  plugins: [
    require('@tailwindcss/line-clamp'),
  ],
}