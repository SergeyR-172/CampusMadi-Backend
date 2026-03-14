import appCss from '@app/styles/global.css?url'
import { createRootRoute, HeadContent, Outlet, Scripts } from '@tanstack/react-router'

export const Route = createRootRoute({
  head: () => ({
    meta: [
      {
        charSet: 'utf-8',
      },
      {
        name: 'viewport',
        content: 'width=device-width, initial-scale=1',
      },
      {
        title: 'CampusMadi',
      },
    ],
    links: [
      {
        rel: 'stylesheet',
        href: appCss,
      },
    ],
  }),
  component: RootComponent,
})

// eslint-disable-next-line @typescript-eslint/naming-convention
function RootComponent() {
  return (
    <html lang="ru" suppressHydrationWarning>
      <head>
        <HeadContent />
      </head>
      <body className="min-h-screen font-sans antialiased">
        <Outlet />
        <Scripts />
      </body>
    </html>
  )
}
