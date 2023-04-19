/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: "jit",
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {
      display: ["group-hover"],
    },
  },
  plugins: [
    require('@tailwindcss/line-clamp'),
  ],
}

