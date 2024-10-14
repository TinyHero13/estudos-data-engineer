import pandas as pd

df = pd.read_html('https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_2024_-_S%C3%A9rie_A')[3]

print(df)