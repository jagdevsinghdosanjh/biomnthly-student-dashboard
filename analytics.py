def calculate_scores(df):
    core_subjects = ['Punjabi', 'Hindi', 'English', 'Math', 'Science', 'Social Science']
    df['Total'] = df[core_subjects].sum(axis=1)
    df['Percentage'] = (df['Total'] / (len(core_subjects) * 20)) * 100
    return df

def get_top_students(df, top_n=10):
    return df.sort_values(by='Percentage', ascending=False).head(top_n)

