# Fontsource submission

Fontsource accepts fonts that are not on Google Fonts if they have a public official source (preferably GitHub) and are licensed under OFL-1.1, Apache-2.0, UFL-1.0 or MIT. LandUI Pro is OFL-1.1.

Before either route, search https://github.com/fontsource/font-files for an existing issue or PR about LandUI Pro.

## Route A: request it (Fontsource packages it)

Open https://github.com/fontsource/font-files/issues/new/choose and pick **➕ Font request**. This is the request as it was entered in the form.

**Title:**

```
Font Request: LandUI Pro (Variable)
```

**Font Name:**

```
LandUI Pro
```

**Link to font source:**

```
Github Link: https://github.com/multiporttm/landui-pro-repo
Font Download Link: https://fontfiles.multiportllc.com/MLFonts/LandUIPro.ttf
```

**Link to font license:**

```
https://github.com/multiporttm/landui-pro-repo/blob/main/OFL.txt
```

**Additional context:**

```
* Font Name: LandUI Pro
* Designer: Multiport
* Source: [github.com/multiporttm/landui-pro-repo](https://github.com/multiporttm/landui-pro-repo)
* License: SIL Open Font License 1.1 ([OFL.txt](https://github.com/multiporttm/landui-pro-repo/blob/main/OFL.txt))
* Category: Sans-serif
* Variable Axes: `opsz` (14–32), `wght` (100–900)
* Styles: Normal
* Subsets: Latin, Latin Extended
* Version: 1.000
* Variable Font File: [LandUIPro[opsz,wght].ttf](https://github.com/multiporttm/landui-pro-repo/blob/main/fonts/variable/LandUIPro%5Bopsz%2Cwght%5D.ttf)
* Webfont File: [LandUIPro[opsz,wght].woff2](https://github.com/multiporttm/landui-pro-repo/blob/main/fonts/webfonts/LandUIPro%5Bopsz%2Cwght%5D.woff2)

LandUI Pro is a variable sans-serif typeface for user interfaces derived from [Inter](https://github.com/rsms/inter), configuring a curated set of OpenType alternate glyphs (`cv05`, `cv06`, `cv08`, `cv10`, `cv11`, `cv12`, `cv13`, `zero`, `ss01`, `ss03`, `ss07`) as defaults.

LandUI Pro vs Inter (top: Inter, bottom: LandUI Pro):
<img width="1100" height="660" alt="landui-pro-vs-inter" src="https://github.com/user-attachments/assets/d4690694-ddf4-4776-9395-f2e8bd231b3e" />
```

The image is the comparison specimen from `documentation/landui-pro-vs-inter.png`, uploaded to GitHub.

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
