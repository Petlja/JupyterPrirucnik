# koristi se invoke komanda za pokretanje taskova (vidi http://pyinvoke.org/, instalira se pip-om)

import os
import shutil

from invoke import task

def remove_files_from_dir(dir):
    for f in os.listdir(dir):
        fpath = os.path.join(dir,f)
        if os.path.isfile(fpath):
            print(f"removing {fpath}")
            os.unlink(fpath)

@task 
def build(c, clean=False):
    base_dir = c.config._project_prefix
    build_dir = os.path.join(base_dir, 'docs')
    img_src_dir = os.path.join(base_dir, 'slike')
    img_build_dir = os.path.join(build_dir, 'slike')

    if clean:
        remove_files_from_dir(build_dir)
        remove_files_from_dir(img_build_dir)

    for f in os.listdir(img_src_dir):
        fsrc = os.path.join(img_src_dir, f)
        fdst = os.path.join(img_build_dir, f)
        print(f"copy {fsrc} -> {fdst}")
        shutil.copyfile(fsrc, fdst)

    with c.cd(base_dir):
        c.run(f"jupyter nbconvert --to html *.ipynb --output-dir {build_dir}")