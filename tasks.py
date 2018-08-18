# koristi se invoke komanda za pokretanje taskova (vidi http://pyinvoke.org/, instalira se pip-om)

import os
from invoke import task

@task 
def build(c, clean=False):
    base_dir = c.config._project_prefix
    docs_dir = os.path.join(base_dir, 'docs')
    if clean:
        for f in os.listdir(docs_dir):
            print(f"removing {f} from {docs_dir}")
            os.unlink(os.path.join(docs_dir,f))
    with c.cd(base_dir):
        c.run(f"jupyter nbconvert --to html *.ipynb --output-dir {docs_dir}")