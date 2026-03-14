# Frontend — документация

## NPM-команды

| Команда           | Описание                                            |
| ----------------- | --------------------------------------------------- |
| `npm run dev`     | Запуск dev-сервера на порту 3000                    |
| `npm run build`   | Сборка продакшн-бандла                              |
| `npm run preview` | Превью продакшн-сборки                              |
| `npm run test`    | Запуск тестов (vitest run)                          |
| `npm run lint`    | Проверка кода через ESLint                          |
| `npm run format`  | Проверка форматирования через Prettier (без записи) |
| `npm run check`   | Форматирование Prettier + автофикс ESLint           |
| `npm run fix`     | Автофикс ESLint + форматирование Prettier           |

> Проект использует `pnpm`. Предпочтительно использовать `pnpm run <команда>`.

---

## Правила написания кода

### Форматирование (Prettier)

- **Точки с запятой**: всегда используются (`semi: true`)
- **Кавычки**: двойные (`singleQuote: false`)
- **Висячие запятые**: везде — в массивах, объектах, параметрах функций (`trailingComma: 'all'`)
- **Длина строки**: максимум 100 символов (`printWidth: 100`)
- **Отступы**: 2 пробела (`tabWidth: 2`)
- **Пробелы в объектных литералах**: `{ foo: bar }` — да (`bracketSpacing: true`)
- **Скобки у стрелочных функций**: всегда — `(x) => x` (`arrowParens: 'always'`)
- **Сортировка классов Tailwind**: автоматическая через `prettier-plugin-tailwindcss`; функции `cva`, `clsx`, `cn` также сортируются

**Файлы, исключённые из форматирования** (`prettierignore`):

- `package-lock.json`, `pnpm-lock.yaml`, `yarn.lock`
- `routeTree.gen.ts` (генерируемый файл TanStack Router)

---

### Стиль кода (ESLint)

#### Функции

- Использовать только **стрелочные функции** (`func-style: expression`)
- Исключение: файлы роутов `src/routes/**/*.tsx|ts` — разрешены function declaration (требование TanStack Router)

#### Именование

| Что                             | Стиль                                       |
| ------------------------------- | ------------------------------------------- |
| Типы, интерфейсы                | `PascalCase`                                |
| Файлы, переменные, параметры    | `camelCase`                                 |
| Константы (`const`)             | `camelCase` \| `UPPER_CASE` \| `PascalCase` |
| Экспортируемые React-компоненты | `PascalCase` (имя начинается с заглавной)   |
| Zod-схемы (`*Schema`)           | `camelCase` \| `UPPER_CASE` \| `PascalCase` |
| API-данные (snake_case поля)    | разрешён `snake_case`                       |
| Неиспользуемые переменные       | префикс `_` (например, `_unused`)           |

#### Импорты

- Импорты **сортируются автоматически** плагином `eslint-plugin-simple-import-sort` — нарушение является ошибкой

#### Прочее

- `console.log` — **предупреждение**; разрешены только `console.warn` и `console.error`
- Неиспользуемые переменные — **ошибка** (кроме тех, что начинаются с `_`)

#### Исключения для shadcn-компонентов

Файлы `src/shared/shadcn/**` — ослаблены правила:

- `func-style` отключён
- `@typescript-eslint/naming-convention` отключён
