from flask import Flask, render_template, send_file, request
import pandas as pd
import urllib
import matplotlib.pyplot as plt
import io
import seaborn as sns
# from lib import get_genres
# import 

app = Flask(__name__)


# df = pd.read_csv('dataset.csv')

@app.route('/')
def exercice2():
    return "hello world"
    # return render_template('exercice2.html', genres=get_genres(df))

# @app.route('/api/items/<genre>/<artiste>/<trier_par>', methods=['GET'])
# def getInfos(genre, artiste, trier_par):
#     df = pd.read_csv('dataset.csv')
#     genre = df.genre.str.contains(genre, case=False)
#     artist_name =  df.artist_name.str.contains(artiste, case=False)
#     sort_by = trier_par

#     df = df.loc[genre & artist_name][:20].reset_index()
#     df = df.sort_values(by=sort_by, ascending=False).to_dict('record')
#     return df


if __name__=='__main__':
    app.run(debug=True)