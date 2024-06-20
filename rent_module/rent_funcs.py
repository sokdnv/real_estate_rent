import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')


def count_plot(df, column_name):
    fig, ax = plt.subplots(figsize=(10, 6))

    sns.countplot(data=df, x=column_name, ax=ax)

    ax.set_ylabel('Количество')
    ax.set_title(f'Распределение значений для {column_name}')


def kde_plot(df, column_name):
    fig, ax = plt.subplots(figsize=(10, 6))

    sns.kdeplot(data=df, x=column_name, ax=ax)

    ax.set_ylabel('Количество')
    ax.set_title(f'Распределение значений для {column_name}')