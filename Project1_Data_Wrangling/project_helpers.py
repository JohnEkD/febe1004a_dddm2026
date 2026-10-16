"""Support for this project's notebook. You do not need to read this file.

Keep it in the same folder as the notebook. The notebook uses it for cells
marked *Just run this cell* that depend on an answer further up:

    with needs('Question 1.1'):     says which question the cell is waiting for
                                    instead of failing with a long error

    checkpoint('q1_1')              reports whether one answer is usable before
                                    the cells that depend on it are reached

    summary('q3_1')                 prints or draws the summary the notebook
                                    shows once a question is answered

The checkpoint tests and the summaries are further down this file. They are
kept here rather than in the notebook so that the notebook stays short, and
`sweep.py` in the grading folder checks they still refer to variables the
project defines.
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
            return False
        if kind is AssertionError:
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


# --------------------------------------------------------------- checkpoints


def checkpoint(question_id):
    """Report whether one answer is usable, before the cells that need it.

    Marks nothing. Prints one of three things: that the question has not been
    answered yet, that it has an answer which is not right, or a short summary
    of the answer so the student can see it is sound.
    """
    spec = CHECKPOINTS.get(question_id)
    if spec is None:
        raise KeyError('no checkpoint is defined for %s' % question_id)

    env = inspect.currentframe().f_back.f_globals
    label, note = spec['question'], spec.get('note')

    unanswered = [n for n in spec['needs']
                  if n not in env or env[n] is Ellipsis]
    if unanswered:
        print('STOP. This cell needs %s finished first.' % label)
        print('Nothing else is wrong: finish that question and run this again.')
        print('(no answer yet for %s)' % ', '.join(unanswered))
        if note:
            print(note)
        return

    try:
        ok = bool(spec['test'](env))
    except Exception as e:
        print('STOP. %s has an answer, but it is not right yet.' % label)
        print('%s: %s' % (type(e).__name__, str(e)[:80]))
        if note:
            print(note)
        return

    if not ok:
        print('STOP. %s has an answer, but it is not right yet.' % label)
        print(spec['why'])
        if note:
            print(note)
        return

    print(spec['report'](env))


CHECKPOINTS = {
    'q1_1': dict(
        question='Question 1.1',
        note='Almost every question below this one depends on it.',
        needs=['birmingham_tenure', 'n_birmingham'],
        test=lambda e: e['n_birmingham'] > 0,
        why='n_birmingham should be the number of Birmingham rows, which is '
            'more than zero.',
        report=lambda e: 'birmingham_tenure looks usable: %d rows'
                         % e['n_birmingham']),

    'q2_1': dict(
        question='Question 2.1',
        note='Questions 2.2 and 5.1 will fail until then.',
        needs=['lookup'],
        test=lambda e: ('Ward' in e['lookup'].labels
                        and 'Council' in e['lookup'].labels),
        why='lookup is missing Ward or Council. Those two names come from the '
            'select and the renames.',
        report=lambda e: 'lookup looks usable: %s' % (e['lookup'].labels,)),

    'q5_1': dict(
        question='Question 5.1',
        note='Question 5.2 will fail until then.',
        needs=['cars'],
        test=lambda e: 'Council' in e['cars'].labels,
        why='cars has no Council column. That column comes from the join.',
        report=lambda e: 'cars looks usable: %d rows, and it has the Council '
                         'column the join adds' % e['cars'].num_rows),
}


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

    env = inspect.currentframe().f_back.f_globals
    label = spec['question']

    unanswered = [n for n in spec['needs']
                  if n not in env or env[n] is Ellipsis]
    if unanswered:
        print('STOP. This cell needs %s finished first.' % label)
        print('Nothing else is wrong: finish that question and run this again.')
        print('(no answer yet for %s)' % ', '.join(unanswered))
        return

    try:
        spec['draw'](env)
    except Exception as e:
        print('STOP. %s has an answer, but it is not right yet.' % label)
        print('%s: %s' % (type(e).__name__, str(e)[:120]))


def _tenure_comparison(e):
    """Ladywood against the city, on owned as well as privately rented."""
    for name, t, rented in [
            ('Ladywood', e['ladywood'], e['ladywood_private_pct']),
            ('Birmingham', e['tenure_wards'], e['birmingham_private_pct'])]:
        owned = sum(t.column('Owned')) / sum(t.column('Households')) * 100
        print('%-11s  owned %5.1f%%   private rented %5.1f%%   neither %5.1f%%'
              % (name, owned, rented, 100 - owned - rented))
    print('Private renting in Ladywood is %.2f times the city figure'
          % e['private_rented_ratio'])


def _ward_histogram(e):
    """Every ward's private renting, with Ladywood marked in red."""
    np, plots, by_ward_pct = e['np'], e['plots'], e['by_ward_pct']
    # SHOWN IN THE NOTEBOOK. These lines are printed in the markdown above the
    # cell that calls summary('q4_2'), so a student can read what draws the
    # picture. sweep.py compares the two and fails if they drift apart.
    by_ward_pct.hist('Private rented %', bins=np.arange(0, 60, 5), unit='%')
    ladywood_pct = by_ward_pct.where('Ward', 'Ladywood').column('Private rented %').item(0)
    plots.scatter(ladywood_pct, 0, color='red', s=60, zorder=3)
    plots.title('Private renting across Birmingham wards')
    plots.show()


def _birmingham_map(e):
    """Every Birmingham LSOA plotted, car-free ones in red, Ladywood ringed."""
    np, plots, Table = e['np'], e['plots'], e['Table']
    centroids = Table.read_table('birmingham_centroids.csv')
    mapped = e['cars_bham'].join('LSOA', centroids)

    car_pct = mapped.column('No car') / mapped.column('Households') * 100
    light = car_pct > 35

    plots.figure(figsize=(7, 7))
    plots.gca().set_axisbelow(True)
    plots.grid(True, color='#dddddd', lw=0.7)
    plots.scatter(mapped.column('Easting')[~light], mapped.column('Northing')[~light],
                  s=14, color='#4477aa', label='under 35% car-free')
    plots.scatter(mapped.column('Easting')[light], mapped.column('Northing')[light],
                  s=14, color='#cc3311', label='over 35% car-free')
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
    plots.title('Car-free households across Birmingham')
    plots.show()


SUMMARIES = {
    'q3_1': dict(
        question='Question 3.1',
        needs=['ladywood_private_pct', 'birmingham_private_pct',
               'private_rented_ratio'],
        draw=_tenure_comparison),

    'q4_2': dict(
        question='Question 4.2',
        needs=['by_ward_pct'],
        draw=_ward_histogram),

    'q5_2': dict(
        question='Question 5.2',
        needs=['cars_bham'],
        draw=_birmingham_map),
}
