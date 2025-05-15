""" deobfuscate the contents of jars/objects which is mostly the music and sound effects
don't release the resulting files as it is a copyright issue according to https://github.com/WangTingZheng/mcp940/issues/2#issuecomment-2883062912 """

import json
from os import path

MC_VERSION = '1.12'

assets_folder = path.join("jars", "assets")
objects_folder= path.join(assets_folder, "objects")
indexes_folder= path.join(assets_folder, "indexes")

def main(argv) -> int:
    mapping_file = open(path.join(indexes_folder, MC_VERSION+'.json'))
    mappings = json.load(mapping_file)['objects']

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
