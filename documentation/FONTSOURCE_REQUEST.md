# Fontsource submission

Fontsource accepts fonts that are not on Google Fonts if they have a public official source (preferably GitHub) and are licensed under OFL-1.1, Apache-2.0, UFL-1.0 or MIT. LandUI Pro is OFL-1.1.

Before either route, search https://github.com/fontsource/font-files for an existing issue or PR about LandUI Pro.

## Route A: request it (Fontsource packages it)

Open an issue at https://github.com/fontsource/font-files/issues/new/choose using the font request template, if there is one.

**Title:** Font request: LandUI Pro

**Body:**

- Font name: LandUI Pro
- Official source: https://github.com/multiporttm/landui-pro-repo
- License: SIL Open Font License 1.1 (OFL.txt in the repository)
- Designer: Multiport
- Type: variable font, axes `opsz` 14–32 and `wght` 100–900, normal style only
- Subsets: latin, latin-ext
- Files: `fonts/variable/LandUIPro[opsz,wght].ttf` (WOFF2 also in `fonts/webfonts/`)
- Notes: Derived from Inter (OFL). Attach `documentation/landui-pro-vs-inter.png`.

## Route B: package it yourself (PR)

From the fontsource/font-files CONTRIBUTING guide:

1. Fork https://github.com/fontsource/font-files.
2. Clone it shallowly and make a branch:
   `git clone https://github.com/<your-fork>/font-files.git --depth 1`
   `git checkout -b landui-pro main`
3. In the repo root, run `bunx fontsource create` and answer the prompts (ID `landui-pro`, family `LandUI Pro`, license OFL-1.1, source URL as above). Add the font files to the generated directory as the CLI tells you.
4. Move the generated package into `fonts/other/`.
5. Run `bun test` to check that the package has every required file.
6. Open a PR to `fontsource/font-files:main` with a Conventional Commit title, e.g. `feat: add LandUI Pro`.
