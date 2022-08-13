from adaptivecards.cards import AdaptiveCard
from adaptivecards.containers import Column, ColumnSet
from adaptivecards.elements import TextBlock


def test_column_set_with_one_column(card: AdaptiveCard):
    column_set = ColumnSet()
    column_one = Column()

    column_set.columns.append(column_one)

    assert column_set.columns[0] == column_one
