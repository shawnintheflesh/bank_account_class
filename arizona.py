import pandas as pd

arizona = pd.read_csv(r'C:/users/admin/Desktop/ArizonaUSFL.txt')
arizona.to_csv(r'C:/users/admin/Desktop/ArizonaUSFL.csv', index=None)



