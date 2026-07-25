# -*- coding: utf-8 -*-
import os
import sys
import json

# 各类型文件对应的目录及 type 值
DIR_TYPE_MAP = {
    "https://kvymin.github.io/CatVodTVJsonEditor/python/":   {"ext": ".py",   "type": 3},
    "https://kvymin.github.io/CatVodTVJsonEditor/javascript/":   {"ext": ".js",   "type": 3},
    
}

def build_sites():
    sites = []
    self_path = os.path.abspath(__file__)

    for dir_path, cfg in DIR_TYPE_MAP.items():
        if not os.path.isdir(dir_path):
            continue

        ext    = cfg["ext"]
        ftype  = cfg["type"]
        folder_name = os.path.basename(dir_path)

        for root, dirs, files in os.walk(dir_path):
            for f in sorted(files):
                if not f.lower().endswith(ext):
                    continue

                full_path = os.path.join(root, f)
                if os.path.abspath(full_path) == self_path:
                    continue

                name_no_ext = f[: f.lower().rfind(ext)]
                rel_path    = os.path.relpath(full_path, dir_path)
                folder_part = os.path.dirname(rel_path)

                if folder_part:
                    name_part = name_no_ext
                else:
                    name_part = folder_name + '☞' + name_no_ext

                sites.append({
                    "key":      f"py_{name_part}",
                    "name":     name_part,
                    "type":     ftype,
                    "searchable":  1,
                    "quickSearch": 1,
                    "api":      f"file://{full_path}"
                })

    return sites

CONFIG = {
    "spider": "",
    "sites": build_sites()
}