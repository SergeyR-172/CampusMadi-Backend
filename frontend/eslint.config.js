//  @ts-check

import { tanstackConfig } from '@tanstack/eslint-config'
import simpleImportSort from 'eslint-plugin-simple-import-sort'

export default [
  ...tanstackConfig,

  // Общие правила проекта
  {
    plugins: {
      'simple-import-sort': simpleImportSort,
    },
    rules: {
      // Отключаем конфликтующие правила из tanstack config
      'import/no-cycle': 'off',
      'import/order': 'off',
      'sort-imports': 'off',
      '@typescript-eslint/array-type': 'off',
      '@typescript-eslint/require-await': 'off',
      'pnpm/json-enforce-catalog': 'off',

      // Сортировка импортов
      'simple-import-sort/imports': 'error',
      'simple-import-sort/exports': 'error',

      // Только стрелочные функции
      'func-style': ['error', 'expression'],

      // console.log → warning
      'no-console': ['warn', { allow: ['warn', 'error'] }],

      // Неиспользуемые переменные
      '@typescript-eslint/no-unused-vars': [
        'error',
        {
          argsIgnorePattern: '^_',
          varsIgnorePattern: '^_',
        },
      ],

      // Нейминг
      '@typescript-eslint/naming-convention': [
        'error',

        // Типы, интерфейсы — PascalCase
        {
          selector: 'typeLike',
          format: ['PascalCase'],
        },

        // Переменные, функции — camelCase
        {
          selector: 'variableLike',
          format: ['camelCase'],
          leadingUnderscore: 'allow',
          trailingUnderscore: 'allow',
        },

        // Константы верхнего уровня — camelCase | UPPER_CASE | PascalCase
        {
          selector: 'variable',
          modifiers: ['const'],
          format: ['camelCase', 'UPPER_CASE', 'PascalCase'],
        },

        // Экспортируемые компоненты (function declaration)
        {
          selector: 'function',
          modifiers: ['exported'],
          format: ['PascalCase'],
          filter: {
            regex: '^[A-Z]',
            match: true,
          },
        },

        // Экспортируемые компоненты (const Button = () => {})
        {
          selector: 'variable',
          modifiers: ['exported', 'const'],
          types: ['function'],
          format: ['PascalCase'],
          filter: {
            regex: '^[A-Z]',
            match: true,
          },
        },

        // Исключения для Zod-схем (*Schema)
        {
          selector: 'variable',
          format: ['camelCase', 'UPPER_CASE', 'PascalCase'],
          filter: {
            regex: '.*Schema$',
            match: true,
          },
        },

        // Разрешить snake_case для данных API
        {
          selector: 'variable',
          format: null,
          filter: {
            regex: '^[_a-z]+$',
            match: true,
          },
        },
      ],
    },
  },

  // Файлы роутов TanStack — разрешить function declaration
  {
    files: ['src/routes/**/*.tsx', 'src/routes/**/*.ts'],
    rules: {
      'func-style': 'off',
    },
  },

  // shadcn компоненты — ослабленные правила
  {
    files: ['src/shared/shadcn/**/*.ts', 'src/shared/shadcn/**/*.tsx'],
    rules: {
      'func-style': 'off',
      '@typescript-eslint/naming-convention': 'off',
    },
  },

  // Игнорируемые файлы
  {
    ignores: ['eslint.config.js', 'prettier.config.js'],
  },
]
