#!/usr/bin/env python3
"""Make LandUI Pro's DEFAULT look different from Inter by promoting a curated set
of Inter's own alternate glyphs into the default character map.

Usage: python3 design.py "build/LandUIPro[opsz,wght].ttf"   (edits in place)
"""
import sys
from fontTools.ttLib import TTFont

# order matters (later features can refine earlier ones, e.g. f.1 -> f.1.ss07)
RECIPE = ["cv11",  # single-storey a
          "cv05",  # l with tail
          "cv08",  # I with serifs
          "cv13",  # alternate t
          "cv06",  # alternate u
          "cv10",  # alternate G
          "cv12",  # alternate f
          "zero",  # slashed zero
          "ss01",  # open digits (1 4 6 9 3)
          "ss03",  # round quotes
          "ss07"]  # square dots/punctuation

def feature_maps(font):
    g = font["GSUB"].table
    maps = {}
    for fr in g.FeatureList.FeatureRecord:
        t = fr.FeatureTag
        if t not in RECIPE:
            continue
        m = maps.setdefault(t, {})
        for li in fr.Feature.LookupListIndex:
            lk = g.LookupList.Lookup[li]
            for st in lk.SubTable:
                if lk.LookupType == 7:
                    st = st.ExtSubTable
                if hasattr(st, "mapping"):
                    m.update(st.mapping)
    return maps

def main(path):
    f = TTFont(path)
    maps = feature_maps(f)
    glyphs = set(f.getGlyphOrder())
    changed = 0
    for sub in f["cmap"].tables:
        for cp, gn in list(sub.cmap.items()):
            new = gn
            for feat in RECIPE:
                nxt = maps.get(feat, {}).get(new)
                if nxt and nxt in glyphs:
                    new = nxt
            if new != gn:
                sub.cmap[cp] = new
                changed += 1
    # new family = version 1.000
    f["head"].fontRevision = 1.0
    nm = f["name"]
    for r in nm.names:
        if r.nameID == 5:
            nm.setName("Version 1.000", 5, r.platformID, r.platEncID, r.langID)
    f.save(path)
    print("remapped", changed, "cmap entries")

if __name__ == "__main__":
    main(sys.argv[1])
