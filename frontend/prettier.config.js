//  @ts-check

/** @type {import('prettier').Config} */
const config = {
  plugins: ['prettier-plugin-tailwindcss'],
  tailwindFunctions: ['cva', 'clsx', 'cn'],
  semi: true,
  singleQuote: false,
  trailingComma: 'all',
  printWidth: 100,
  tabWidth: 2,
  bracketSpacing: true,
  arrowParens: 'always',
}

export default config
