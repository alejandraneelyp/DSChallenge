def delay_rate(df, grouping_var, width = 15):
    fig, ax = plt.subplots()
    temp = pd.DataFrame(df.groupby(grouping_var)["atraso_15"].sum() / df.groupby(grouping_var).size() * 100).reset_index()
    ax = sns.barplot(x=grouping_var, y=temp[0], data=temp).set(title = 'Tasa de atrasos por {}'.format(grouping_var))
    fig.set_figwidth(width)
    plt.ylabel('Tasa de atrasos (%)')
    plt.xticks(rotation=90)
    return fig.show()