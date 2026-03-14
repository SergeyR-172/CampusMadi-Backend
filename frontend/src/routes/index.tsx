import { createFileRoute } from '@tanstack/react-router'
import { HomePage } from '@pages/home/index.ts'

export const Route = createFileRoute('/')({ component: HomePage })
