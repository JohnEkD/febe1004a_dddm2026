"""Support for this project's notebook. You do not need to read this file.

Keep it in the same folder as the notebook. The notebook uses it for cells
marked *Just run this cell* that depend on an answer further up:

    with needs('Question 1.2'):     says which question the cell is waiting for
                                    instead of failing with a long error

    summary('q4_1')                 draws the map the notebook shows once a
                                    question is answered

This project has no checkpoint cells, so this file holds `needs` and
`summary`. The same
`needs` class is in Project 1's folder; `sweep.py` checks the two copies have
not drifted apart.
"""
import inspect


class needs:
    """Run a cell that depends on an earlier answer.

    Used as:

        with needs('Question 2.1'):
            ...the cell's code...

    If the code fails because an answer further up is missing, this prints a
    short note naming that question instead of a traceback.
    """

    def __init__(self, question, note=None):
        self.question, self.note = question, note

    def __enter__(self):
        return self

    def __exit__(self, kind, value, tb):
        if kind is None:
            return False
        if not issubclass(kind, Exception):
            return False        # let Ctrl-C and the like through untouched
        if kind is AssertionError:
            # the answer exists but is not right, so do not tell the student
            # the question is unfinished or that nothing else is wrong
            print('STOP. %s has an answer, but it is not right yet.'
                  % self.question)
            print(str(value)[:140])
        else:
            print('STOP. This cell needs %s finished first.' % self.question)
            print('Nothing else is wrong: finish that question and run this '
                  'again.')
            print('(%s)' % (str(value)[:90] or kind.__name__))
        if self.note:
            print(self.note)
        return True


# ------------------------------------------------------------------ summaries


def summary(question_id):
    """Print or draw the summary the notebook shows once a question is done.

    Marks nothing, and changes nothing the student has written. It only
    displays their own answers, so the cell that calls it is one line.

    If the answer is missing it names the question to finish, exactly as
    `needs` does, rather than failing with a traceback.
    """
    spec = SUMMARIES.get(question_id)
    if spec is None:
        raise KeyError('no summary is defined for %s' % question_id)

    # the student's variables live in the notebook, not in this module
    env = inspect.currentframe().f_back.f_globals
    label = spec['question']

    unanswered = [n for n in spec['needs']
                  if n not in env or env[n] is Ellipsis]
    if unanswered:
        print('STOP. This cell needs %s finished first.' % label)
        print('Nothing else is wrong: finish that question and run this again.')
        print('(no answer yet for %s)' % ', '.join(unanswered))
        return

    # The names exist and are not blank, so anything failing now is a wrong
    # answer and not a missing one. A bare `with needs(...)` cannot tell those
    # apart unless the failure is an AssertionError, and would tell a student
    # who has answered the question to go and finish it.
    try:
        spec['draw'](env)
    except Exception as e:
        print('STOP. %s has an answer, but it is not right yet.' % label)
        print('%s: %s' % (type(e).__name__, str(e)[:120]))


def _ladywood_map(e):
    """Birmingham, with the student's own ten most similar neighbourhoods."""
    np, plots, Table = e['np'], e['plots'], e['Table']
    centroids = Table.read_table('birmingham_centroids.csv')
    mapped = e['lsoas'].join('LSOA', centroids)
    # the ten from the student's own closest_ten, not a fresh calculation, so
    # the map shows what they actually produced
    near = e['closest_ten'].select('LSOA').join('LSOA', centroids)

    plots.figure(figsize=(7, 7))
    plots.gca().set_axisbelow(True)
    plots.grid(True, color='#dddddd', lw=0.7)
    plots.scatter(mapped.column('Easting'), mapped.column('Northing'),
                  s=12, color='#bbbbbb', label='all Birmingham')
    plots.scatter(near.column('Easting'), near.column('Northing'),
                  s=55, color='#cc3311', label='ten most similar')
    lady_map = mapped.where('Ward', 'Ladywood')
    plots.scatter(lady_map.column('Easting'), lady_map.column('Northing'),
                  s=70, facecolors='none', edgecolors='black', linewidths=1.5,
                  label='Ladywood')
    plots.gca().set_aspect('equal')

    ticks_x = np.arange(400000, 420000, 5000)
    ticks_y = np.arange(280000, 305000, 5000)
    plots.xticks(ticks_x, [str(int(v / 1000)) for v in ticks_x])
    plots.yticks(ticks_y, [str(int(v / 1000)) for v in ticks_y])
    plots.xlabel('Easting (km)')
    plots.ylabel('Northing (km)')

    plots.legend(loc='upper left', frameon=False)
    plots.title("Neighbourhoods most like Ladywood")
    plots.show()


SUMMARIES = {
    'q4_1': dict(
        question='Question 4.1',
        needs=['closest_ten'],
        draw=_ladywood_map),
}
