# KPI calculation script

def calculate_kpis(df):

    df['total_discharges'] = (
        df['cured'] +
        df['death'] +
        df['default'] +
        df['non_response']
    )

    df['cure_rate'] = df['cured'] / df['total_discharges']
    df['death_rate'] = df['death'] / df['total_discharges']
    df['default_rate'] = df['default'] / df['total_discharges']

    return df
