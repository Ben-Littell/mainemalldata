import numpy as np
import matplotlib.pyplot as plt
import statistics as stats
import pandas as pd
import func


d_df = pd.read_csv('customer_data.csv')
d_df.columns = ['id', 'gender', 'age', 'income', 'score']

ma_l = d_df[d_df['gender'] == 'Male'].age.values.tolist()
fa_l = d_df[d_df['gender'] == 'Female'].age.values.tolist()

min_l = d_df[d_df['gender'] == 'Male'].income.values.tolist()
fin_l = d_df[d_df['gender'] == 'Female'].income.values.tolist()

ms_l = d_df[d_df['gender'] == 'Male'].score.values.tolist()
fs_l = d_df[d_df['gender'] == 'Female'].score.values.tolist()

mid_l = d_df[d_df['gender'] == 'Male'].id.values.tolist()
fid_l = d_df[d_df['gender'] == 'Female'].id.values.tolist()


# male in-s (25, 20), (25, 70), (55, 50), (85, 15), (85, 80)
# female in-s (25, 20), (25, 80), (55, 50), (90, 20), (90, 80)
m_ins_d, m_ins_c = func.main(min_l, ms_l, centroids=((25, 20), (25, 70), (55, 50), (85, 15), (85, 80)))
f_ins_d, f_ins_c = func.main(fin_l, fs_l, centroids=((25, 20), (25, 80), (55, 50), (90, 20), (90, 80)))
m_in_d_stats = func.dict_stats(min_l, m_ins_d, keys=m_ins_c)
m_s_d_stats = func.dict_stats(ms_l, m_ins_d, keys=m_ins_c)
f_in_d_stats = func.dict_stats(fin_l, m_ins_d, keys=m_ins_c)
print(m_in_d_stats)

male_in_a = func.corcoeff(min_l, ma_l)
female_in_a = func.corcoeff(fin_l, fa_l)
male_a_s = func.corcoeff(ma_l, ms_l)
female_a_s = func.corcoeff(fa_l, fs_l)

print(male_a_s)
print(male_in_a)
print(female_a_s)
print(female_in_a)

