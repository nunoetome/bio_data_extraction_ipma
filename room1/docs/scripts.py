"""

# List of workers on the room1


- worker_ipma_rss_bolsas.py
- worker_ipma_rss_cimp.py
- worker_ipma_rss_comunicados.py
- worker_ipma_rss_comuns.py
- worker_ipma_rss_dirigentes.py
- worker_ipma_rss_investigacao.py
- worker_ipma_rss_mobilidade.py
- worker_ipma_rss_news.py

All this files share the same base code, with some changes 
in the constants and the functions that are called, this are used
to to configure the worker to download the rss data from the
specific rss feed intro a specific folder.

Plus, there are some to have custom made functions and changes:

## Scripts whith custom functions:

This custom changes should be register in the change log and in the
.py file itself

### RSS links to files download

- worker_ipma_rss_bolsas.py
- worker_ipma_rss_investigacao.py
downloding the files from the rss feed and saving them in the folder

- worker_ipma_rss_cimp.py
- worker_ipma_rss_news.py
Has links but they are not being downloaded


### RSS whidout links to files detected

- worker_ipma_rss_comunicados.py

    

- worker_ipma_rss_mobilidade.py

- worker_ipma_rss_dirigentes.py
- worker_ipma_rss_comuns.py




The tipical rss feed from this origin is a rss feed with links to files
for every of them we have a custom function to download the files and register
the new file link inside the <item> tag of the rss feed, identified by the
<link-internal> tag.

The file names use the mask:
ipma_rss_bolsas + pub_date + '-' + original_file_name

pub_date is formatted as: AAAAMMDD-HHMM so it is easy to sort the files by date and time avoiding duplicated names

ipma_rss_bolsas + AAAAMMDD-HHMM + original_file_name

ex:
ipma_rss_bolsas20240723-0001-IPMA-2024-013-BIPD.pdf


"""

