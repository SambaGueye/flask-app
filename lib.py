from flask import Flask, render_template, send_file, request
import pandas as pd
import urllib
import matplotlib.pyplot as plt
import io
import seaborn as sns

def get_genres(df):
    genres = df['genre'].unique()

    genres_music = []
    for genre in genres:
        val = genre.split(',')
        for i in val:
            if i not in genres_music:
                genres_music.append(i)
    return genres_music