module.exports = {
    purge: [],
    theme: {
      extend: {
        colors:{}
      }
    },
    variants: {},
    plugins: [
      require('@tailwindcss/typography'),
      require('@tailwindcss/ui')({
      layout: 'sidebar',
    })
  ],
  }
  