"""empty message

Revision ID: a0b1016579db
Revises: 77458c0c3124
Create Date: 2021-03-19 19:50:26.400186

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a0b1016579db'
down_revision = '77458c0c3124'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Word',
    *[sa.Column('word', sa.String(), nullable=False),
    sa.Column('HGI_positiv', sa.Integer(), nullable=True),
    sa.Column('HGI_negativ', sa.Integer(), nullable=True),
    sa.Column('HGI_pstv', sa.Integer(), nullable=True),
    sa.Column('HGI_affil', sa.Integer(), nullable=True),
    sa.Column('HGI_ngtv', sa.Integer(), nullable=True),
    sa.Column('HGI_hostile', sa.Integer(), nullable=True),
    sa.Column('HGI_strong', sa.Integer(), nullable=True),
    sa.Column('HGI_power', sa.Integer(), nullable=True),
    sa.Column('HGI_weak', sa.Integer(), nullable=True),
    sa.Column('HGI_submit', sa.Integer(), nullable=True),
    sa.Column('HGI_active', sa.Integer(), nullable=True),
    sa.Column('HGI_passive', sa.Integer(), nullable=True),
    sa.Column('HGI_pleasur', sa.Integer(), nullable=True),
    sa.Column('HGI_pain', sa.Integer(), nullable=True),
    sa.Column('HGI_feel', sa.Integer(), nullable=True),
    sa.Column('HGI_arousal', sa.Integer(), nullable=True),
    sa.Column('HGI_emot', sa.Integer(), nullable=True),
    sa.Column('HGI_virtue', sa.Integer(), nullable=True),
    sa.Column('HGI_vice', sa.Integer(), nullable=True),
    sa.Column('HGI_ovrst', sa.Integer(), nullable=True),
    sa.Column('HGI_undrst', sa.Integer(), nullable=True),
    sa.Column('HGI_academ', sa.Integer(), nullable=True),
    sa.Column('HGI_doctrin', sa.Integer(), nullable=True),
    sa.Column('HGI_econ2', sa.Integer(), nullable=True),
    sa.Column('HGI_exch', sa.Integer(), nullable=True),
    sa.Column('HGI_econ', sa.Integer(), nullable=True),
    sa.Column('HGI_exprsv', sa.Integer(), nullable=True),
    sa.Column('HGI_legal', sa.Integer(), nullable=True),
    sa.Column('HGI_milit', sa.Integer(), nullable=True),
    sa.Column('HGI_polit2', sa.Integer(), nullable=True),
    sa.Column('HGI_polit', sa.Integer(), nullable=True),
    sa.Column('HGI_relig', sa.Integer(), nullable=True),
    sa.Column('HGI_role', sa.Integer(), nullable=True),
    sa.Column('HGI_coll', sa.Integer(), nullable=True),
    sa.Column('HGI_work', sa.Integer(), nullable=True),
    sa.Column('HGI_ritual', sa.Integer(), nullable=True),
    sa.Column('HGI_socrel', sa.Integer(), nullable=True),
    sa.Column('HGI_race', sa.Integer(), nullable=True),
    sa.Column('HGI_kin2', sa.Integer(), nullable=True),
    sa.Column('HGI_male', sa.Integer(), nullable=True),
    sa.Column('HGI_female', sa.Integer(), nullable=True),
    sa.Column('HGI_nonadlt', sa.Integer(), nullable=True),
    sa.Column('HGI_hu', sa.Integer(), nullable=True),
    sa.Column('HGI_ani', sa.Integer(), nullable=True),
    sa.Column('HGI_place', sa.Integer(), nullable=True),
    sa.Column('HGI_social', sa.Integer(), nullable=True),
    sa.Column('HGI_region', sa.Integer(), nullable=True),
    sa.Column('HGI_route', sa.Integer(), nullable=True),
    sa.Column('HGI_aquatic', sa.Integer(), nullable=True),
    sa.Column('HGI_land', sa.Integer(), nullable=True),
    sa.Column('HGI_sky', sa.Integer(), nullable=True),
    sa.Column('HGI_object', sa.Integer(), nullable=True),
    sa.Column('HGI_tool', sa.Integer(), nullable=True),
    sa.Column('HGI_food', sa.Integer(), nullable=True),
    sa.Column('HGI_vehicle', sa.Integer(), nullable=True),
    sa.Column('HGI_bldgpt', sa.Integer(), nullable=True),
    sa.Column('HGI_comnobj', sa.Integer(), nullable=True),
    sa.Column('HGI_natobj', sa.Integer(), nullable=True),
    sa.Column('HGI_bodypt', sa.Integer(), nullable=True),
    sa.Column('HGI_comform', sa.Integer(), nullable=True),
    sa.Column('HGI_com', sa.Integer(), nullable=True),
    sa.Column('HGI_say', sa.Integer(), nullable=True),
    sa.Column('HGI_need', sa.Integer(), nullable=True),
    sa.Column('HGI_goal', sa.Integer(), nullable=True),
    sa.Column('HGI_try', sa.Integer(), nullable=True),
    sa.Column('HGI_means', sa.Integer(), nullable=True),
    sa.Column('HGI_persist', sa.Integer(), nullable=True),
    sa.Column('HGI_complet', sa.Integer(), nullable=True),
    sa.Column('HGI_fail', sa.Integer(), nullable=True),
    sa.Column('HGI_natrpro', sa.Integer(), nullable=True),
    sa.Column('HGI_begin', sa.Integer(), nullable=True),
    sa.Column('HGI_vary', sa.Integer(), nullable=True),
    sa.Column('HGI_increas', sa.Integer(), nullable=True),
    sa.Column('HGI_decreas', sa.Integer(), nullable=True),
    sa.Column('HGI_finish', sa.Integer(), nullable=True),
    sa.Column('HGI_stay', sa.Integer(), nullable=True),
    sa.Column('HGI_rise', sa.Integer(), nullable=True),
    sa.Column('HGI_exert', sa.Integer(), nullable=True),
    sa.Column('HGI_fetch', sa.Integer(), nullable=True),
    sa.Column('HGI_travel', sa.Integer(), nullable=True),
    sa.Column('HGI_fall', sa.Integer(), nullable=True),
    sa.Column('HGI_think', sa.Integer(), nullable=True),
    sa.Column('HGI_know', sa.Integer(), nullable=True),
    sa.Column('HGI_causal', sa.Integer(), nullable=True),
    sa.Column('HGI_ought', sa.Integer(), nullable=True),
    sa.Column('HGI_perceiv', sa.Integer(), nullable=True),
    sa.Column('HGI_compare', sa.Integer(), nullable=True),
    sa.Column('HGI_eval2', sa.Integer(), nullable=True),
    sa.Column('HGI_eval', sa.Integer(), nullable=True),
    sa.Column('HGI_solve', sa.Integer(), nullable=True),
    sa.Column('HGI_abs2', sa.Integer(), nullable=True),
    sa.Column('HGI_abs', sa.Integer(), nullable=True),
    sa.Column('HGI_quality', sa.Integer(), nullable=True),
    sa.Column('HGI_quan', sa.Integer(), nullable=True),
    sa.Column('HGI_numb', sa.Integer(), nullable=True),
    sa.Column('HGI_ord', sa.Integer(), nullable=True),
    sa.Column('HGI_card', sa.Integer(), nullable=True),
    sa.Column('HGI_freq', sa.Integer(), nullable=True),
    sa.Column('HGI_dist', sa.Integer(), nullable=True),
    sa.Column('HGI_time2', sa.Integer(), nullable=True),
    sa.Column('HGI_time', sa.Integer(), nullable=True),
    sa.Column('HGI_space', sa.Integer(), nullable=True),
    sa.Column('HGI_pos', sa.Integer(), nullable=True),
    sa.Column('HGI_dim', sa.Integer(), nullable=True),
    sa.Column('HGI_rel', sa.Integer(), nullable=True),
    sa.Column('HGI_color', sa.Integer(), nullable=True),
    sa.Column('HGI_self', sa.Integer(), nullable=True),
    sa.Column('HGI_our', sa.Integer(), nullable=True),
    sa.Column('HGI_you', sa.Integer(), nullable=True),
    sa.Column('HGI_name', sa.Integer(), nullable=True),
    sa.Column('HGI_yes', sa.Integer(), nullable=True),
    sa.Column('HGI_no', sa.Integer(), nullable=True),
    sa.Column('HGI_negate', sa.Integer(), nullable=True),
    sa.Column('HGI_intrj', sa.Integer(), nullable=True),
    sa.Column('HGI_iav', sa.Integer(), nullable=True),
    sa.Column('HGI_dav', sa.Integer(), nullable=True),
    sa.Column('HGI_sv', sa.Integer(), nullable=True),
    sa.Column('HGI_ipadj', sa.Integer(), nullable=True),
    sa.Column('HGI_indadj', sa.Integer(), nullable=True),
    sa.Column('HGI_powgain', sa.Integer(), nullable=True),
    sa.Column('HGI_powloss', sa.Integer(), nullable=True),
    sa.Column('HGI_powends', sa.Integer(), nullable=True),
    sa.Column('HGI_powaren', sa.Integer(), nullable=True),
    sa.Column('HGI_powcon', sa.Integer(), nullable=True),
    sa.Column('HGI_powcoop', sa.Integer(), nullable=True),
    sa.Column('HGI_powaupt', sa.Integer(), nullable=True),
    sa.Column('HGI_powpt', sa.Integer(), nullable=True),
    sa.Column('HGI_powdoct', sa.Integer(), nullable=True),
    sa.Column('HGI_powauth', sa.Integer(), nullable=True),
    sa.Column('HGI_powoth', sa.Integer(), nullable=True),
    sa.Column('HGI_powtot', sa.Integer(), nullable=True),
    sa.Column('HGI_rcethic', sa.Integer(), nullable=True),
    sa.Column('HGI_rcrelig', sa.Integer(), nullable=True),
    sa.Column('HGI_rcgain', sa.Integer(), nullable=True),
    sa.Column('HGI_rcloss', sa.Integer(), nullable=True),
    sa.Column('HGI_rcends', sa.Integer(), nullable=True),
    sa.Column('HGI_rctot', sa.Integer(), nullable=True),
    sa.Column('HGI_rspgain', sa.Integer(), nullable=True),
    sa.Column('HGI_rsploss', sa.Integer(), nullable=True),
    sa.Column('HGI_rspoth', sa.Integer(), nullable=True),
    sa.Column('HGI_rsptot', sa.Integer(), nullable=True),
    sa.Column('HGI_affgain', sa.Integer(), nullable=True),
    sa.Column('HGI_affloss', sa.Integer(), nullable=True),
    sa.Column('HGI_affpt', sa.Integer(), nullable=True),
    sa.Column('HGI_affoth', sa.Integer(), nullable=True),
    sa.Column('HGI_afftot', sa.Integer(), nullable=True),
    sa.Column('HGI_wltpt', sa.Integer(), nullable=True),
    sa.Column('HGI_wlttran', sa.Integer(), nullable=True),
    sa.Column('HGI_wltoth', sa.Integer(), nullable=True),
    sa.Column('HGI_wlttot', sa.Integer(), nullable=True),
    sa.Column('HGI_wlbgain', sa.Integer(), nullable=True),
    sa.Column('HGI_wlbloss', sa.Integer(), nullable=True),
    sa.Column('HGI_wlbphys', sa.Integer(), nullable=True),
    sa.Column('HGI_wlbpsyc', sa.Integer(), nullable=True),
    sa.Column('HGI_wlbpt', sa.Integer(), nullable=True),
    sa.Column('HGI_wlbtot', sa.Integer(), nullable=True),
    sa.Column('HGI_enlgain', sa.Integer(), nullable=True),
    sa.Column('HGI_enlloss', sa.Integer(), nullable=True),
    sa.Column('HGI_enlends', sa.Integer(), nullable=True),
    sa.Column('HGI_enlpt', sa.Integer(), nullable=True),
    sa.Column('HGI_enloth', sa.Integer(), nullable=True),
    sa.Column('HGI_enltot', sa.Integer(), nullable=True),
    sa.Column('HGI_sklasth', sa.Integer(), nullable=True),
    sa.Column('HGI_sklpt', sa.Integer(), nullable=True),
    sa.Column('HGI_skloth', sa.Integer(), nullable=True),
    sa.Column('HGI_skltot', sa.Integer(), nullable=True),
    sa.Column('HGI_trngain', sa.Integer(), nullable=True),
    sa.Column('HGI_trnloss', sa.Integer(), nullable=True),
    sa.Column('HGI_tranlw', sa.Integer(), nullable=True),
    sa.Column('HGI_meanslw', sa.Integer(), nullable=True),
    sa.Column('HGI_endslw', sa.Integer(), nullable=True),
    sa.Column('HGI_arenalw', sa.Integer(), nullable=True),
    sa.Column('HGI_ptlw', sa.Integer(), nullable=True),
    sa.Column('HGI_nation', sa.Integer(), nullable=True),
    sa.Column('HGI_anomie', sa.Integer(), nullable=True),
    sa.Column('HGI_negaff', sa.Integer(), nullable=True),
    sa.Column('HGI_posaff', sa.Integer(), nullable=True),
    sa.Column('HGI_surelw', sa.Integer(), nullable=True),
    sa.Column('HGI_if', sa.Integer(), nullable=True),
    sa.Column('HGI_notlw', sa.Integer(), nullable=True),
    sa.Column('HGI_timespc', sa.Integer(), nullable=True),
    sa.Column('HGI_formlw', sa.Integer(), nullable=True),
    sa.Column('LIWC_function', sa.Integer(), nullable=True),
    sa.Column('LIWC_pronoun', sa.Integer(), nullable=True),
    sa.Column('LIWC_ppron', sa.Integer(), nullable=True),
    sa.Column('LIWC_i', sa.Integer(), nullable=True),
    sa.Column('LIWC_we', sa.Integer(), nullable=True),
    sa.Column('LIWC_you', sa.Integer(), nullable=True),
    sa.Column('LIWC_shehe', sa.Integer(), nullable=True),
    sa.Column('LIWC_they', sa.Integer(), nullable=True),
    sa.Column('LIWC_ipron', sa.Integer(), nullable=True),
    sa.Column('LIWC_article', sa.Integer(), nullable=True),
    sa.Column('LIWC_prep', sa.Integer(), nullable=True),
    sa.Column('LIWC_auxverb', sa.Integer(), nullable=True),
    sa.Column('LIWC_adverb', sa.Integer(), nullable=True),
    sa.Column('LIWC_conj', sa.Integer(), nullable=True),
    sa.Column('LIWC_negate', sa.Integer(), nullable=True),
    sa.Column('LIWC_verb', sa.Integer(), nullable=True),
    sa.Column('LIWC_adj', sa.Integer(), nullable=True),
    sa.Column('LIWC_compare', sa.Integer(), nullable=True),
    sa.Column('LIWC_interrog', sa.Integer(), nullable=True),
    sa.Column('LIWC_number', sa.Integer(), nullable=True),
    sa.Column('LIWC_quant', sa.Integer(), nullable=True),
    sa.Column('LIWC_affect', sa.Integer(), nullable=True),
    sa.Column('LIWC_posemo', sa.Integer(), nullable=True),
    sa.Column('LIWC_negemo', sa.Integer(), nullable=True),
    sa.Column('LIWC_anx', sa.Integer(), nullable=True),
    sa.Column('LIWC_anger', sa.Integer(), nullable=True),
    sa.Column('LIWC_sad', sa.Integer(), nullable=True),
    sa.Column('LIWC_social', sa.Integer(), nullable=True),
    sa.Column('LIWC_family', sa.Integer(), nullable=True),
    sa.Column('LIWC_friend', sa.Integer(), nullable=True),
    sa.Column('LIWC_female', sa.Integer(), nullable=True),
    sa.Column('LIWC_male', sa.Integer(), nullable=True),
    sa.Column('LIWC_cogproc', sa.Integer(), nullable=True),
    sa.Column('LIWC_insight', sa.Integer(), nullable=True),
    sa.Column('LIWC_cause', sa.Integer(), nullable=True),
    sa.Column('LIWC_discrep', sa.Integer(), nullable=True),
    sa.Column('LIWC_tentat', sa.Integer(), nullable=True),
    sa.Column('LIWC_certain', sa.Integer(), nullable=True),
    sa.Column('LIWC_differ', sa.Integer(), nullable=True),
    sa.Column('LIWC_percept', sa.Integer(), nullable=True),
    sa.Column('LIWC_see', sa.Integer(), nullable=True),
    sa.Column('LIWC_hear', sa.Integer(), nullable=True),
    sa.Column('LIWC_feel', sa.Integer(), nullable=True),
    sa.Column('LIWC_bio', sa.Integer(), nullable=True),
    sa.Column('LIWC_body', sa.Integer(), nullable=True),
    sa.Column('LIWC_health', sa.Integer(), nullable=True),
    sa.Column('LIWC_sexual', sa.Integer(), nullable=True),
    sa.Column('LIWC_ingest', sa.Integer(), nullable=True),
    sa.Column('LIWC_drives', sa.Integer(), nullable=True),
    sa.Column('LIWC_affiliation', sa.Integer(), nullable=True),
    sa.Column('LIWC_achiev', sa.Integer(), nullable=True),
    sa.Column('LIWC_power', sa.Integer(), nullable=True),
    sa.Column('LIWC_reward', sa.Integer(), nullable=True),
    sa.Column('LIWC_risk', sa.Integer(), nullable=True),
    sa.Column('LIWC_focuspast', sa.Integer(), nullable=True),
    sa.Column('LIWC_focuspresent', sa.Integer(), nullable=True),
    sa.Column('LIWC_focusfuture', sa.Integer(), nullable=True),
    sa.Column('LIWC_relativ', sa.Integer(), nullable=True),
    sa.Column('LIWC_motion', sa.Integer(), nullable=True),
    sa.Column('LIWC_space', sa.Integer(), nullable=True),
    sa.Column('LIWC_time', sa.Integer(), nullable=True),
    sa.Column('LIWC_work', sa.Integer(), nullable=True),
    sa.Column('LIWC_leisure', sa.Integer(), nullable=True),
    sa.Column('LIWC_home', sa.Integer(), nullable=True),
    sa.Column('LIWC_money', sa.Integer(), nullable=True),
    sa.Column('LIWC_relig', sa.Integer(), nullable=True),
    sa.Column('LIWC_death', sa.Integer(), nullable=True),
    sa.Column('LIWC_informal', sa.Integer(), nullable=True),
    sa.Column('LIWC_swear', sa.Integer(), nullable=True),
    sa.Column('LIWC_netspeak', sa.Integer(), nullable=True),
    sa.Column('LIWC_assent', sa.Integer(), nullable=True),
    sa.Column('LIWC_nonflu', sa.Integer(), nullable=True),
    sa.Column('LIWC_filler', sa.Integer(), nullable=True),
    sa.Column('MRC_kf_freq', sa.Float(), nullable=True),
    sa.Column('MRC_kf_nsamp', sa.Float(), nullable=True),
    sa.Column('MRC_tl_freq', sa.Float(), nullable=True),
    sa.Column('MRC_brown_freq', sa.Float(), nullable=True),
    sa.Column('MRC_fam', sa.Float(), nullable=True),
    sa.Column('MRC_conc', sa.Float(), nullable=True),
    sa.Column('MRC_imag', sa.Float(), nullable=True),
    sa.Column('MRC_meanc', sa.Float(), nullable=True),
    sa.Column('MRC_meanp', sa.Float(), nullable=True),
    sa.Column('MRC_aoa', sa.Float(), nullable=True),
    sa.Column('NRC_positive', sa.Integer(), nullable=True),
    sa.Column('NRC_negative', sa.Integer(), nullable=True),
    sa.Column('NRC_anger', sa.Integer(), nullable=True),
    sa.Column('NRC_anticipation', sa.Integer(), nullable=True),
    sa.Column('NRC_disgust', sa.Integer(), nullable=True),
    sa.Column('NRC_fear', sa.Integer(), nullable=True),
    sa.Column('NRC_joy', sa.Integer(), nullable=True),
    sa.Column('NRC_sadness', sa.Integer(), nullable=True),
    sa.Column('NRC_surprise', sa.Integer(), nullable=True),
    sa.Column('NRC_trust', sa.Integer(), nullable=True),
    sa.Column('S_visual', sa.Float(), nullable=True),
    sa.Column('S_auditory', sa.Float(), nullable=True),
    sa.Column('S_gustatory', sa.Float(), nullable=True),
    sa.Column('S_olfactory', sa.Float(), nullable=True),
    sa.Column('S_tactile', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('word')],
    schema='public'
    )
    op.drop_table('Word', schema='personality')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Word',
    *[sa.Column('word', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('HGI_positiv', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_negativ', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_pstv', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_affil', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_ngtv', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_hostile', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_strong', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_power', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_weak', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_submit', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_active', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_passive', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_pleasur', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_pain', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_feel', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_arousal', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_emot', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_virtue', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_vice', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_ovrst', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_undrst', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_academ', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_doctrin', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_econ2', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_exch', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_econ', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_exprsv', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_legal', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_milit', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_polit2', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_polit', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_relig', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_role', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_coll', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_work', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_ritual', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_socrel', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_race', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_kin2', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_male', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_female', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_nonadlt', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_hu', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_ani', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_place', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_social', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_region', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_route', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_aquatic', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_land', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_sky', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_object', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_tool', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_food', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_vehicle', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_bldgpt', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_comnobj', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_natobj', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_bodypt', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_comform', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_com', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_say', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_need', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_goal', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_try', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_means', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_persist', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_complet', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_fail', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_natrpro', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_begin', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_vary', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_increas', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_decreas', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_finish', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_stay', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_rise', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_exert', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_fetch', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_travel', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_fall', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_think', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_know', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_causal', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_ought', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_perceiv', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_compare', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_eval2', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_eval', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_solve', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_abs2', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_abs', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_quality', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_quan', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_numb', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_ord', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_card', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_freq', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_dist', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_time2', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_time', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_space', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_pos', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_dim', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_rel', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_color', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_self', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_our', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_you', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_name', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_yes', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_no', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_negate', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_intrj', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_iav', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_dav', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_sv', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_ipadj', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_indadj', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_powgain', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_powloss', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_powends', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_powaren', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_powcon', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_powcoop', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_powaupt', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_powpt', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_powdoct', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_powauth', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_powoth', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_powtot', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_rcethic', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_rcrelig', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_rcgain', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_rcloss', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_rcends', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_rctot', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_rspgain', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_rsploss', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_rspoth', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_rsptot', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_affgain', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_affloss', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_affpt', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_affoth', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_afftot', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_wltpt', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_wlttran', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_wltoth', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_wlttot', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_wlbgain', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_wlbloss', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_wlbphys', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_wlbpsyc', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_wlbpt', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_wlbtot', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_enlgain', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_enlloss', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_enlends', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_enlpt', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_enloth', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_enltot', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_sklasth', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_sklpt', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_skloth', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_skltot', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_trngain', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_trnloss', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_tranlw', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_meanslw', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_endslw', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_arenalw', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_ptlw', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_nation', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_anomie', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_negaff', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_posaff', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_surelw', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_if', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_notlw', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_timespc', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HGI_formlw', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_function', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_pronoun', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_ppron', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_i', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_we', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_you', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_shehe', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_they', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_ipron', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_article', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_prep', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_auxverb', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_adverb', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_conj', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_negate', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_verb', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_adj', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_compare', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_interrog', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_number', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_quant', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_affect', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_posemo', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_negemo', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_anx', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_anger', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_sad', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_social', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_family', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_friend', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_female', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_male', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_cogproc', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_insight', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_cause', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_discrep', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_tentat', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_certain', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_differ', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_percept', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_see', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_hear', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_feel', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_bio', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_body', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_health', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_sexual', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_ingest', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_drives', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_affiliation', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_achiev', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_power', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_reward', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_risk', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_focuspast', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_focuspresent', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_focusfuture', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_relativ', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_motion', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_space', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_time', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_work', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_leisure', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_home', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_money', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_relig', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_death', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_informal', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_swear', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_netspeak', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_assent', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_nonflu', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LIWC_filler', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('MRC_kf_freq', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('MRC_kf_nsamp', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('MRC_tl_freq', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('MRC_brown_freq', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('MRC_fam', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('MRC_conc', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('MRC_imag', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('MRC_meanc', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('MRC_meanp', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('MRC_aoa', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('NRC_positive', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('NRC_negative', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('NRC_anger', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('NRC_anticipation', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('NRC_disgust', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('NRC_fear', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('NRC_joy', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('NRC_sadness', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('NRC_surprise', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('NRC_trust', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('S_visual', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('S_auditory', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('S_gustatory', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('S_olfactory', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('S_tactile', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('word', name='Word_pkey')],
    schema='personality'
    )
    op.drop_table('Word', schema='public')
    # ### end Alembic commands ###
