import "./globals.css";
import type { ReactNode } from "react";

const links = [
  { href: "/", label: "Overview" },
  { href: "/library", label: "Library" },
  { href: "/topics", label: "Topics" },
  { href: "/graph", label: "Graph" },
  { href: "/youtube", label: "YouTube" },
  { href: "/digests", label: "Digests" },
  { href: "/search", label: "Search" },
];

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body>
        <div className="shell">
          <header className="siteHeader">
            <div>
              <p className="eyebrow">Research Collector</p>
              <h1>Frontier Literature Knowledge System</h1>
            </div>
            <nav className="siteNav">
              {links.map((link) => (
                <a key={link.href} href={link.href}>
                  {link.label}
                </a>
              ))}
            </nav>
          </header>
          <main>{children}</main>
        </div>
      </body>
    </html>
  );
}
