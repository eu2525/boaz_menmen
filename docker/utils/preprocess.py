import pandas as pd

def json_to_df(response_text):
    df = pd.DataFrame(response_text['result_data']['poi_section']['list'])
    df['nm'] = df.apply(lambda x: f"{x['nm']} ({x['branch']})" if pd.notna(x['branch']) else x['nm'], axis=1)
    df = df.drop(columns=['branch', 'my_favorites', 'favorites_cnt', 'review_cnt', 'recommend_cnt', 'display_review','dingco_flag', 'review_total_cnt', 'review_list'])
    
    return df