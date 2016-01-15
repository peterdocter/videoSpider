"""Cut subject and movie tables

Revision ID: 54b5db82884c
Revises: 049480272df5
Create Date: 2016-01-14 19:57:21.196800

"""

# revision identifiers, used by Alembic.
revision = '54b5db82884c'
down_revision = '049480272df5'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('movies', schema=None) as batch_op:
        batch_op.add_column(sa.Column('crawler_sort', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('crawler_tag', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('duration', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('imdb_number', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('official_site', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('types', sa.String(), nullable=True))
        batch_op.drop_column('mainland_pubdate')
        batch_op.drop_column('schedule_url')
        batch_op.drop_column('mobile_url')
        batch_op.drop_column('seasons_count')
        batch_op.drop_column('clip_urls')
        batch_op.drop_column('alt')
        batch_op.drop_column('douban_site')
        batch_op.drop_column('website')
        batch_op.drop_column('aka')
        batch_op.drop_column('pubdate')
        batch_op.drop_column('blooper_urls')
        batch_op.drop_column('tag')
        batch_op.drop_column('trailer_urls')
        batch_op.drop_column('sort')
        batch_op.drop_column('popular_reviews')
        batch_op.drop_column('durations')
        batch_op.drop_column('pubdates')
        batch_op.drop_column('comments_count')
        batch_op.drop_column('reviews_count')

    with op.batch_alter_table('subjects', schema=None) as batch_op:
        batch_op.add_column(sa.Column('aliases', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('douban_rate', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('douban_rating', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('douban_ratings_count', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('pubdate', sa.String(), nullable=True))
        batch_op.drop_column('rating')
        batch_op.drop_column('collect_count')
        batch_op.drop_column('images')
        batch_op.drop_column('ratings_count')
        batch_op.drop_column('wish_count')
        batch_op.drop_column('original_title')
        batch_op.drop_column('do_count')
        batch_op.drop_column('rate')
        batch_op.drop_column('image')

    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('subjects', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('rate', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('do_count', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('original_title', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('wish_count', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('ratings_count', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('images', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('collect_count', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('rating', sa.VARCHAR(), nullable=True))
        batch_op.drop_column('pubdate')
        batch_op.drop_column('douban_ratings_count')
        batch_op.drop_column('douban_rating')
        batch_op.drop_column('douban_rate')
        batch_op.drop_column('aliases')

    with op.batch_alter_table('movies', schema=None) as batch_op:
        batch_op.add_column(sa.Column('reviews_count', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('comments_count', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('pubdates', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('durations', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('popular_reviews', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('sort', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('trailer_urls', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('tag', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('blooper_urls', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('pubdate', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('aka', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('website', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('douban_site', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('alt', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('clip_urls', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('seasons_count', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('mobile_url', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('schedule_url', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('mainland_pubdate', sa.VARCHAR(), nullable=True))
        batch_op.drop_column('types')
        batch_op.drop_column('official_site')
        batch_op.drop_column('imdb_number')
        batch_op.drop_column('duration')
        batch_op.drop_column('crawler_tag')
        batch_op.drop_column('crawler_sort')

    ### end Alembic commands ###
