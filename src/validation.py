# Visualization script

def validate_caseload(df):

    df['expected_end'] = (
        df['opening_caseload'] +
        df['admissions'] -
        df['total_discharges']
    )

    df['caseload_match'] = (
        df['expected_end'] == df['end_caseload']
    )

    return df
