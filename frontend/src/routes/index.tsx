import { HomePage } from '@pages/home/index.ts'
import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/')({ component: HomePage })
