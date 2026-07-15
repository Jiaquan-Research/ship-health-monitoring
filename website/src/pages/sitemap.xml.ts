const pages = [
  "",
  "status",
  "research",
  "projects",
  "projects/ship-health-monitoring",
  "projects/ship-health-monitoring/marine-package",
  "projects/ship-health-monitoring/boundaries",
  "projects/ship-health-monitoring/framework",
  "projects/ship-health-monitoring/validation",
  "projects/ship-health-monitoring/external-validation",
  "projects/ship-health-monitoring/deep-research",
  "review",
  "review/deep-research",
  "review/external-validation",
  "machine",
  "machine/manifest",
  "machine/public-manifest",
  "machine/retrieval-manifest",
  "machine/governance",
  "governance",
  "about"
];

export function GET() {
  const body = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${pages
    .map((page) => `  <url><loc>https://jqhe.uk/${page}</loc></url>`)
    .join("\n")}\n</urlset>`;
  return new Response(body, { headers: { "Content-Type": "application/xml" } });
}
