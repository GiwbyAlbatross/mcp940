""" deobfuscate the contents of jars/objects which is mostly the music and sound effects
don't release the resulting files as it is a copyright issue according to https://github.com/WangTingZheng/mcp940/issues/2#issuecomment-2883062912 """

import json
import pathlib
import shutil

MC_VERSION = '1.12'

assets_folder = pathlib.Path("jars", "assets")
objects_folder= pathlib.Path(assets_folder, "objects")
indexes_folder= pathlib.Path(assets_folder, "indexes")
result_folder = pathlib.Path("objects")

def main(argv) -> int:
    mapping_file = open(indexes_folder / MC_VERSION+'.json')
    mappings = json.load(mapping_file)['objects']
    for file in mappings:
        file_id = mappings[file]['hash']
        hashdir = objects_folder / file_id[:2]
        fileloc = hashdir / file_id
        endpath = result_folder / file
        end_dir = endpath.parents[0]

        end_dir.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(fileloc, endpath)
        

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
