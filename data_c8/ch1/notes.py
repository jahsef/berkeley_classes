import requests

from datascience import Table

import numpy as np


huck_finn_url = 'https://www.inferentialthinking.com/data/huck_finn.txt'
huck_finn_text = requests.get(huck_finn_url).text
huck_finn_chapters = huck_finn_text.split('CHAPTER ')[44:]

table = Table().with_column('Chapters', huck_finn_chapters)

print(table)


counts = Table().with_columns([
    
    [x, np.cumsum(np.char.count(huck_finn_chapters, x))] 
    for x in ["Jim", "Tom", "Huck"]
])

cum_counts = counts.with_column('Chapter', np.arange(1,44,1))

cum_counts.plot(column_for_xticks=3)
